/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50617
 Source Host           : localhost:3306
 Source Schema         : jsp_info

 Target Server Type    : MySQL
 Target Server Version : 50617
 File Encoding         : 65001

 Date: 06/12/2022 08:14:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `id` int(40) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `author` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `price` double NULL DEFAULT NULL,
  `image` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `category_id` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `category_id`(`category_id`) USING BTREE,
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES (1, '《西游记》', '吴承恩', 89, 'img/xiyouji.jpg', '我国四大名著之一', '1');
INSERT INTO `book` VALUES (2, '《马列主义》', '马克思', 100, 'img/ma.jpg', '社会主义主要的精神支柱', '2');
INSERT INTO `book` VALUES (3, '《穿透历史》', '田余庆', 79, 'img/history.jpg', '田余庆，北京大学历史系教授，主要研究方向为中国古代史、秦汉魏晋南北朝史。代表作为《东晋门阀政治》、《秦汉魏晋史探微》和《拓跋史探》。', '3');
INSERT INTO `book` VALUES (4, '《自私的基因》', '理查德·道金斯', 120, 'img/self.jpg', '我们从哪里来，又将到哪里去。生命有何意义，我们该如何认知自己？这本书是实实在在的认知科学，复制、变异和淘汰简单的三种机制可以演变出所有大千世界生命现象里的林林总总。', '4');
INSERT INTO `book` VALUES (5, '《西方战争艺术》', '阿彻琼斯', 56, 'img/bottle.jpg', '战争也是一种艺术，不单是血腥，想知道希特勒如何成为战争天才的吗？快来看这本书吧！', '5');
INSERT INTO `book` VALUES (6, '《资本论》', '马克思', 130, 'img/ziben.jpg', '以剩余价值为中心，对资本主义进行了彻底的批判。第一卷研究了资本的生产过程，分析了剩余价值的生产问题。第二卷在资本生产过程的基础上研究了资本的流通过程，分析了剩余价值的实现问题。第三卷讲述了资本主义生产的总过程，分别研究了资本和剩余价值的具体形式。这一卷讲述的内容达到了资本的生产过程、流通过程和分配过程的高度统一，分析了剩余价值的分配问题。', '6');

-- ----------------------------
-- Table structure for car
-- ----------------------------
DROP TABLE IF EXISTS `car`;
CREATE TABLE `car`  (
  `id` int(40) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `b_id` int(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `pb_id`(`b_id`) USING BTREE,
  INDEX `pu_name`(`u_name`) USING BTREE,
  CONSTRAINT `pb_id` FOREIGN KEY (`b_id`) REFERENCES `book` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `pu_name` FOREIGN KEY (`u_name`) REFERENCES `user` (`username`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of car
-- ----------------------------

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category`  (
  `id` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `category_description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`type`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', '古典名著', '比较古老的一类书，但比较经典');
INSERT INTO `category` VALUES ('2', '哲学', '比较抽象，不容易学懂');
INSERT INTO `category` VALUES ('3', '社会科学', '走近科学，不要迷信，你值得看一看');
INSERT INTO `category` VALUES ('4', '自然科学', '探索自然的奥秘，大自然是我们的母亲，我们要向大自然学习');
INSERT INTO `category` VALUES ('5', '军事', '了解国家动态，做军事强国，人人有责');
INSERT INTO `category` VALUES ('6', '经济', '了解生活中的经济分类');

-- ----------------------------
-- Table structure for fileload
-- ----------------------------
DROP TABLE IF EXISTS `fileload`;
CREATE TABLE `fileload`  (
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `time` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of fileload
-- ----------------------------
INSERT INTO `fileload` VALUES ('04-JSP基本语法.pptx', '2022-12-03', '10:14:14', 'upload/04-JSP基本语法.pptx');
INSERT INTO `fileload` VALUES ('citydata.js', '2022-12-03', '10:14:56', 'upload/citydata.js');
INSERT INTO `fileload` VALUES ('jquery-3.3.1.min.js', '2022-12-03', '10:15:40', 'upload/jquery-3.3.1.min.js');
INSERT INTO `fileload` VALUES ('实验11-JSP中的文件上传与下载.docx', '2022-12-03', '10:13:44', 'upload/实验11-JSP中的文件上传与下载.docx');
INSERT INTO `fileload` VALUES ('实验2： Log工具及活动的使用.pdf', '2022-12-03', '10:00:10', 'upload/实验2： Log工具及活动的使用.pdf');

-- ----------------------------
-- Table structure for information
-- ----------------------------
DROP TABLE IF EXISTS `information`;
CREATE TABLE `information`  (
  `hobby` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `degree` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` int(3) NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id` int(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of information
-- ----------------------------
INSERT INTO `information` VALUES ('登山,健身', '本科', 23, '张三', '男', 1);
INSERT INTO `information` VALUES ('旅游,游泳', '本科', 22, '王思瑶', '女', 4);
INSERT INTO `information` VALUES ('健身,游泳', '研究生', 20, '吴语', '女', 6);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `username` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` int(10) NULL DEFAULT NULL,
  PRIMARY KEY (`username`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('12345', '12345678', '13284947678', '1278353938@qq.com', '浙江省杭州市', NULL);
INSERT INTO `user` VALUES ('lisi', 'E10ADC3949BA59ABBE56E057F20F883E', '123456', '5555', '成都', NULL);
INSERT INTO `user` VALUES ('zhangsan', '123', '沙河', '123456@qq.com', '重庆', NULL);

-- ----------------------------
-- View structure for book_category
-- ----------------------------
DROP VIEW IF EXISTS `book_category`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `book_category` AS select `category`.`type` AS `type`,`category`.`category_description` AS `category_description`,`book`.`description` AS `description`,`book`.`image` AS `image`,`book`.`price` AS `price`,`book`.`author` AS `author`,`book`.`name` AS `name`,`book`.`id` AS `id` from (`book` join `category` on((`book`.`category_id` = `category`.`id`))) ;

SET FOREIGN_KEY_CHECKS = 1;
