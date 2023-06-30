$(function(){
    // 全选 or 全取消
    $('.checkAll').click(function(event) {
        var table = $(this).closest('.f-result');  // 获取当前表格
        var rowCheckboxes = table.find('.rowCheckbox');  // 获取表格内所有行的复选框

        rowCheckboxes.prop('checked', $(this).prop('checked'));
        event.stopPropagation();

        updateSelectedRowText();
    });

    // 点击表格每一行的checkbox
    $('.rowCheckbox').click(function(event) {
        var table = $(this).closest('.f-result');  // 获取当前表格
        var tableCheckAll = table.find('.checkAll');  // 获取表格的表头复选框
        var rowCheckboxes = table.find('.rowCheckbox');  // 获取表格内所有行的复选框

        tableCheckAll.prop('checked', rowCheckboxes.length === rowCheckboxes.filter(':checked').length);
        event.stopPropagation();

        updateSelectedRowText();
    });

    // 点击表格行(行内任意位置)
    $('.checkline').click(function() {
        $(this).find('.rowCheckbox').click();
    });


    // 获取磁盘路径选择框和已选路径列表
    const diskSelect = document.getElementById('disk-select');
    const selectedPaths = document.getElementById('selected-paths');

    // 监听选择框的change事件
    diskSelect.addEventListener('change', function() {
        console.log('Selected Path:', this.value);
        // 清空已选路径列表
        selectedPaths.innerHTML = '';

        // 获取选中的磁盘路径
        const selectedPath = this.value;

        // 创建新的列表项，并将选中的路径添加到已选路径列表中
        const listItem = document.createElement('li');
        listItem.textContent = selectedPath;
        selectedPaths.appendChild(listItem);

        // 发送AJAX请求获取下一级目录
        getTopLevelDirectories(selectedPath);
    });

    // 发送AJAX请求获取下一级目录
    function getTopLevelDirectories(directory) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `/get_top_level_directories/?directory=${encodeURIComponent(directory)}`, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                const directories = response.directories;
                updateSelectOptions(directories);
            }
        };
        xhr.send();
    }

    // 更新选择框的选项
    function updateSelectOptions(directories) {
        const select = document.getElementById('disk-select');
        const currentPath = select.value;

        // 清空选择框选项
        select.innerHTML = '<option value="" disabled selected></option>';

        directories.forEach(function(directory) {
            const option = document.createElement('option');
            option.value = option.value = currentPath.endsWith('\\') ? `${currentPath}${directory}` : `${currentPath}\\${directory}`;
            option.textContent = directory;
            select.appendChild(option);
        });
    }

});

function updateSelectedRowText() {
    var selectedRows = $('.rowCheckbox:checked').closest('.checkline');
    var selectedRowText = '';

    selectedRows.each(function() {
        var rowData = $(this).find('td:nth-child(3)').text();
        selectedRowText += rowData + ', ';
    });

    selectedRowText = selectedRowText.slice(0, -2); // 去除最后的逗号和空格

    $('#selectedRowText').text(selectedRowText);
}

function saveResults() {
    var selectedRows = [];
    var tables = document.querySelectorAll('.f-result');  // 获取所有的table元素
    tables.forEach(function (table) {
        var checkboxes = table.querySelectorAll('input[type="checkbox"]:checked');
        if (checkboxes.length === 0) {
            return;  // 跳过没有选中行的table
        }

        var file_name = table.querySelector('.f-s-fn').innerText;  // 获取文件名
        selectedRows.push('FileName: ' + file_name);  // 将文件名添加到选中行数组中
        var tableHeaders = Array.from(table.querySelectorAll('th:not(:first-child)')).map(function (th) {
            return th.innerText;
        });
        selectedRows.push(tableHeaders.join('\t'));  // 将表头添加到选中行数组中

        var tableHeaderLength = tableHeaders.join('\t').length*2;  // 获取表头长度
        var separatorLine = '-'.repeat(tableHeaderLength);  // 生成与表头长度相同的横线字符串
        selectedRows.push(separatorLine);  // 添加横线作为分隔

        checkboxes.forEach(function (checkbox) {
            var row = checkbox.parentNode.parentNode;
            var rowText = Array.from(row.querySelectorAll('td:nth-child(2), td:nth-child(3)')).map(function (td) {
                return td.innerText;
            });
            if(rowText!='')
                selectedRows.push(rowText.join('\t'));  // 将选中行的文本内容添加到选中行数组中
        });
        selectedRows.push('');  // 添加空行作为分隔
    });

    // 将选中的文本内容发送给后端视图函数进行处理
    fetch('/save_results/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // 用于跳过Django的CSRF保护,使用名为"csrftoken"的Cookie值
        },
        body: JSON.stringify({ 'selected_rows': selectedRows })
    }).then(function (response) {
        return response.blob();
    }).then(function (blob) {
        // 创建并下载txt文件
        var url = window.URL.createObjectURL(blob);
        var link = document.createElement('a');
        link.href = url;
        link.download = 'selected_results.txt';
        link.click();
    });
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}