$(function(){
    // 全选 or 全取消
    $('#checkAll').click(function(event) {
        var tr_checkbox = $('table tbody tr').find('input[type=checkbox]');
        tr_checkbox.prop('checked', $(this).prop('checked'));
        // 阻止向上冒泡，以防再次触发点击操作
        event.stopPropagation();

        updateSelectedRowText();
    });

    // 点击表格每一行的checkbox，表格所有选中的checkbox数 = 表格行数时，则将表头的‘checkAll’单选框置为选中，否则置为未选中
    $('.checkline').find('input[type=checkbox]').click(function(event) {
        var tbr = $('.checkline');
        $('#checkAll').prop('checked', tbr.find('input[type=checkbox]:checked').length == tbr.length ? true : false);
        // 阻止向上冒泡，以防再次触发点击操作
        event.stopPropagation();

        updateSelectedRowText();
    });

    // 点击表格行(行内任意位置)，触发选中或取消选中该行的checkbox
    $('.checkline').click(function() {
        $(this).find('input[type=checkbox]').click();
    });
});
function updateSelectedRowText() {
    var selectedRows = $('.checkline').has('input[type=checkbox]:checked');
    var selectedRowText = '';

    selectedRows.each(function() {
        var rowData = $(this).find('td:nth-child(3)').text();
        selectedRowText += rowData + ', ';
    });

    selectedRowText = selectedRowText.slice(0, -2); // 去除最后的逗号和空格

    $('#selectedRowText').text(selectedRowText);
}
