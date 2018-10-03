/*
Navicat MySQL Data Transfer

Source Server         : MySql_localhost
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : software_development_methods

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2018-09-23 23:02:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES ('5', 'administrator');
INSERT INTO `auth_group` VALUES ('1', 'Project leader');
INSERT INTO `auth_group` VALUES ('3', 'Project Member');
INSERT INTO `auth_group` VALUES ('4', 'Researcher');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES ('7', '1', '23');
INSERT INTO `auth_group_permissions` VALUES ('4', '1', '24');
INSERT INTO `auth_group_permissions` VALUES ('5', '1', '26');
INSERT INTO `auth_group_permissions` VALUES ('6', '1', '27');
INSERT INTO `auth_group_permissions` VALUES ('3', '3', '11');
INSERT INTO `auth_group_permissions` VALUES ('8', '3', '23');
INSERT INTO `auth_group_permissions` VALUES ('17', '5', '1');
INSERT INTO `auth_group_permissions` VALUES ('18', '5', '2');
INSERT INTO `auth_group_permissions` VALUES ('19', '5', '3');
INSERT INTO `auth_group_permissions` VALUES ('13', '5', '4');
INSERT INTO `auth_group_permissions` VALUES ('16', '5', '5');
INSERT INTO `auth_group_permissions` VALUES ('14', '5', '6');
INSERT INTO `auth_group_permissions` VALUES ('20', '5', '7');
INSERT INTO `auth_group_permissions` VALUES ('21', '5', '8');
INSERT INTO `auth_group_permissions` VALUES ('22', '5', '9');
INSERT INTO `auth_group_permissions` VALUES ('23', '5', '10');
INSERT INTO `auth_group_permissions` VALUES ('24', '5', '11');
INSERT INTO `auth_group_permissions` VALUES ('25', '5', '12');
INSERT INTO `auth_group_permissions` VALUES ('26', '5', '13');
INSERT INTO `auth_group_permissions` VALUES ('27', '5', '14');
INSERT INTO `auth_group_permissions` VALUES ('28', '5', '15');
INSERT INTO `auth_group_permissions` VALUES ('29', '5', '16');
INSERT INTO `auth_group_permissions` VALUES ('30', '5', '17');
INSERT INTO `auth_group_permissions` VALUES ('31', '5', '18');
INSERT INTO `auth_group_permissions` VALUES ('32', '5', '19');
INSERT INTO `auth_group_permissions` VALUES ('33', '5', '20');
INSERT INTO `auth_group_permissions` VALUES ('34', '5', '21');
INSERT INTO `auth_group_permissions` VALUES ('35', '5', '22');
INSERT INTO `auth_group_permissions` VALUES ('36', '5', '23');
INSERT INTO `auth_group_permissions` VALUES ('37', '5', '24');
INSERT INTO `auth_group_permissions` VALUES ('38', '5', '25');
INSERT INTO `auth_group_permissions` VALUES ('39', '5', '26');
INSERT INTO `auth_group_permissions` VALUES ('40', '5', '27');
INSERT INTO `auth_group_permissions` VALUES ('41', '5', '28');
INSERT INTO `auth_group_permissions` VALUES ('42', '5', '29');
INSERT INTO `auth_group_permissions` VALUES ('43', '5', '30');
INSERT INTO `auth_group_permissions` VALUES ('44', '5', '31');
INSERT INTO `auth_group_permissions` VALUES ('45', '5', '32');
INSERT INTO `auth_group_permissions` VALUES ('46', '5', '33');
INSERT INTO `auth_group_permissions` VALUES ('47', '5', '34');
INSERT INTO `auth_group_permissions` VALUES ('48', '5', '35');

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add project', '7', 'add_project');
INSERT INTO `auth_permission` VALUES ('20', 'Can change project', '7', 'change_project');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete project', '7', 'delete_project');
INSERT INTO `auth_permission` VALUES ('22', 'Can query user', '4', 'query_user');
INSERT INTO `auth_permission` VALUES ('23', 'Can add happy level', '8', 'add_happylevel');
INSERT INTO `auth_permission` VALUES ('24', 'Can change happy level', '8', 'change_happylevel');
INSERT INTO `auth_permission` VALUES ('25', 'Can delete happy level', '8', 'delete_happylevel');
INSERT INTO `auth_permission` VALUES ('26', 'can query happy level', '8', 'query_happylevel');
INSERT INTO `auth_permission` VALUES ('27', 'can export happy level', '8', 'export_happylevel');
INSERT INTO `auth_permission` VALUES ('28', 'Can add task batch', '9', 'add_taskbatch');
INSERT INTO `auth_permission` VALUES ('29', 'Can change task batch', '9', 'change_taskbatch');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete task batch', '9', 'delete_taskbatch');
INSERT INTO `auth_permission` VALUES ('31', 'Can add task state', '10', 'add_taskstate');
INSERT INTO `auth_permission` VALUES ('32', 'Can change task state', '10', 'change_taskstate');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete task state', '10', 'delete_taskstate');
INSERT INTO `auth_permission` VALUES ('34', 'can query task state', '10', 'query_taskstate');
INSERT INTO `auth_permission` VALUES ('35', 'can export task state', '10', 'export_taskstate');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `project_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `nationality` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hobby` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_email` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$Tmzof6V54Wou$x/UBaSn4XMjosjFg7CP2FGpvnmVHifXMxPfSmfMNFLs=', '2018-09-23 10:57:00.002000', '1', 'admin', 'aa', 'b', 'x1980p@gmail.com', '1', '1', '2018-09-03 02:17:11.709000', null, 'USA', 'running', null);
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$36000$zA7RzySm0r13$xMKB3X3NxKnKT/7KZiOPXBYx7+5/XysPB0ASqVJqfrs=', '2018-09-23 10:57:14.277000', '0', 'user1', 'Tong', 'Xing', 'x1980p@gmail.com', '1', '1', '2018-09-03 02:19:31.000000', '3', 'UK', 'swimming', '0');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$36000$m5YfUod6fiOn$v0AiBQY4XqbrLWNztQVXAuw+QdlJSaCxHmSxLdTLqV8=', '2018-09-23 10:53:40.189000', '0', 'user2', '', '', '', '1', '1', '2018-09-04 04:23:33.000000', '2', '', '', '1');
INSERT INTO `auth_user` VALUES ('4', 'pbkdf2_sha256$36000$2JILuJMth8WN$e3AC4TpXhvvkeBTr9Yh8BlKrG0s12V1McTPmOqkhfBA=', null, '0', 'user3', '', '', '', '0', '1', '2018-09-12 01:23:23.820000', null, null, null, null);
INSERT INTO `auth_user` VALUES ('6', 'pbkdf2_sha256$36000$D69T5BbL4B8z$+WHMpSaTCc4kX9Km4XBsUOysKUUlKyxCg+hpOm1GCSk=', '2018-09-22 08:35:15.091000', '0', 'user4', '', '', '', '1', '1', '2018-09-22 08:22:23.000000', '2', '', '', '0');
INSERT INTO `auth_user` VALUES ('7', 'pbkdf2_sha256$36000$W3OjiN1sLr6s$yRnqaMNK2EWNuIDOjTMDOAtdM5yBcC1Wi6tNhusuit8=', null, '0', 'user5', '', '', '', '0', '1', '2018-09-23 10:54:13.246000', null, null, null, '0');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
INSERT INTO `auth_user_groups` VALUES ('6', '2', '3');
INSERT INTO `auth_user_groups` VALUES ('7', '3', '5');
INSERT INTO `auth_user_groups` VALUES ('5', '6', '5');

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
INSERT INTO `auth_user_user_permissions` VALUES ('2', '2', '11');
INSERT INTO `auth_user_user_permissions` VALUES ('3', '2', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('1', '3', '11');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-09-03 02:19:31.435000', '2', 'user1', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-09-03 02:20:07.249000', '2', 'user1', '2', '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"role\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-09-04 03:26:49.252000', '1', 'Project object', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2018-09-04 03:31:38.677000', '2', 'Project object', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2018-09-04 03:55:30.588000', '1', 'group1', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2018-09-04 03:55:40.664000', '2', 'group2', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2018-09-04 04:22:15.491000', '3', 'Project object', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2018-09-04 04:23:33.355000', '3', 'user2', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2018-09-04 04:30:32.907000', '3', 'Project object', '2', '[{\"changed\": {\"fields\": [\"is_active\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2018-09-04 04:33:09.538000', '2', 'group2', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2018-09-04 05:17:01.881000', '2', 'Project object', '2', '[{\"changed\": {\"fields\": [\"is_active\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2018-09-04 05:32:22.562000', '2', 'Project object', '2', '[{\"changed\": {\"fields\": [\"is_active\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2018-09-04 05:58:56.606000', '3', 'Project object', '2', '[{\"changed\": {\"fields\": [\"is_active\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2018-09-04 06:22:10.644000', '1', 'porject1', '2', '[{\"changed\": {\"fields\": [\"is_active\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2018-09-04 06:23:05.163000', '3', 'group2', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2018-09-04 06:23:24.591000', '2', 'user1', '2', '[{\"changed\": {\"fields\": [\"project\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2018-09-04 07:54:04.161000', '1', 'Project leader', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2018-09-04 07:54:27.243000', '3', 'Project Member', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2018-09-04 07:54:44.584000', '4', 'Researcher', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2018-09-04 09:05:10.424000', '3', 'user2', '2', '[{\"changed\": {\"fields\": [\"is_staff\", \"project\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2018-09-04 22:12:00.633000', '2', 'user1', '2', '[{\"changed\": {\"fields\": [\"nationality\", \"hobby\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2018-09-06 03:32:28.824000', '22', 'auth | user | Can query user', '1', '[{\"added\": {}}]', '3', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2018-09-06 03:42:31.342000', '1', 'Project leader', '2', '[]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2018-09-06 03:42:54.160000', '3', 'Project Member', '2', '[]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2018-09-06 03:43:38.894000', '2', 'user1', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2018-09-06 03:43:53.752000', '3', 'user2', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2018-09-06 04:07:07.426000', '2', 'user1', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2018-09-06 04:07:16.307000', '3', 'user2', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2018-09-06 04:38:44.506000', '2', 'project2', '2', '[{\"changed\": {\"fields\": [\"is_active\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2018-09-06 04:39:12.026000', '3', 'user2', '2', '[{\"changed\": {\"fields\": [\"project\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2018-09-06 23:36:32.030000', '1', 'Project leader', '2', '[]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2018-09-06 23:36:50.438000', '3', 'Project Member', '2', '[]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2018-09-12 01:23:23.858000', '4', 'user3', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2018-09-17 05:55:03.438000', '3', 'user2', '2', '[{\"changed\": {\"fields\": [\"is_email\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2018-09-22 07:58:00.258000', '5', 'administrator', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2018-09-22 08:02:35.324000', '2', 'user1', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2018-09-22 08:13:08.957000', '5', 'user4', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2018-09-22 08:13:59.379000', '5', 'user4', '2', '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"project\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2018-09-22 08:21:55.722000', '5', 'user4', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2018-09-22 08:22:23.934000', '6', 'user4', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2018-09-22 08:26:10.935000', '6', 'u4', '2', '[{\"changed\": {\"fields\": [\"username\", \"project\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2018-09-22 08:26:58.936000', '2', 'user1', '2', '[{\"changed\": {\"fields\": [\"is_staff\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2018-09-22 08:27:10.537000', '6', 'u4', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('44', '2018-09-22 08:28:36.108000', '5', 'administrator', '2', '[]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('45', '2018-09-22 08:29:53.736000', '6', 'u4', '2', '[{\"changed\": {\"fields\": [\"is_staff\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('46', '2018-09-22 08:30:19.656000', '6', 'aaaaa', '1', '[{\"added\": {}}]', '2', '6');
INSERT INTO `django_admin_log` VALUES ('47', '2018-09-22 08:33:37.066000', '6', 'user4', '2', '[{\"changed\": {\"fields\": [\"username\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('48', '2018-09-22 08:33:52.925000', '6', 'aaaaa', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('49', '2018-09-22 08:34:01.409000', '5', 'administrator', '2', '[]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('50', '2018-09-23 10:45:02.494000', '2', 'user1', '2', '[]', '4', '2');
INSERT INTO `django_admin_log` VALUES ('51', '2018-09-23 10:52:06.019000', '2', 'user1', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('52', '2018-09-23 10:52:24.826000', '5', 'administrator', '2', '[]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('53', '2018-09-23 10:52:49.659000', '3', 'user2', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('54', '2018-09-23 10:53:27.217000', '3', 'user2', '2', '[]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('55', '2018-09-23 10:54:13.283000', '7', 'user5', '1', '[{\"added\": {}}]', '4', '3');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('8', 'HappyManagement', 'happylevel');
INSERT INTO `django_content_type` VALUES ('9', 'HappyManagement', 'taskbatch');
INSERT INTO `django_content_type` VALUES ('10', 'HappyManagement', 'taskstate');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'Sys', 'project');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-09-03 02:06:30.230000');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-09-03 02:06:31.852000');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-09-03 02:06:32.294000');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-09-03 02:06:32.306000');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2018-09-03 02:06:32.512000');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2018-09-03 02:06:32.638000');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2018-09-03 02:06:32.771000');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2018-09-03 02:06:32.782000');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2018-09-03 02:06:32.895000');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2018-09-03 02:06:32.898000');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2018-09-03 02:06:32.912000');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2018-09-03 02:06:33.050000');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_auto_20180902_1542', '2018-09-03 02:06:33.208000');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0010_auto_20180902_1648', '2018-09-03 02:06:33.504000');
INSERT INTO `django_migrations` VALUES ('15', 'sessions', '0001_initial', '2018-09-03 02:06:33.599000');
INSERT INTO `django_migrations` VALUES ('16', 'Sys', '0001_initial', '2018-09-04 03:24:29.985000');
INSERT INTO `django_migrations` VALUES ('17', 'Sys', '0002_auto_20180904_1603', '2018-09-04 04:04:34.198000');
INSERT INTO `django_migrations` VALUES ('18', 'HappyManagement', '0001_initial', '2018-09-06 08:39:30.811000');
INSERT INTO `django_migrations` VALUES ('19', 'HappyManagement', '0002_auto_20180906_2122', '2018-09-06 09:22:57.632000');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('0e9b6k9u3sr4dz45ry03je8nw5kw7cz1', 'YjE1M2ZmZTc4MDFiYzMzZjhkZjk2NWJmYTYzMTEyYWZkOTI5MzJiMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjdjNTAwYWYyZDg5Y2NhYmYwMGU1OTM4MmUzYzRkYWEyNTUzZTRiMjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-09-19 08:34:59.572000');
INSERT INTO `django_session` VALUES ('28kgsp66uye8fw583fo5w3bi283qukqa', 'M2FlOGNmMzdlZGQ0Y2MyOWQ1MzcyZGIyNmU0OTk2ZTU2OGZkYjE4MTp7Il9hdXRoX3VzZXJfaGFzaCI6IjhiNDliNGVlMjFkNGI2NTZhMTE5YWVmZTZhZTE5MTJjYTZlMmIwOTYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-09-19 10:20:26.282000');
INSERT INTO `django_session` VALUES ('2isii2d0sktm06f19qt4jn8qmugvvfd1', 'ZTEyNzk4NGFjMjc0NzQwNGVmYWE1MTRjZjQxZWRjOTZjMjQyZWI4NDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiR0VUX1BBUkFNIjp7InBhZ2VOdW0iOiIxIiwicGFnZVNpemUiOiIxMCJ9LCJfYXV0aF91c2VyX2hhc2giOiI4YjQ5YjRlZTIxZDRiNjU2YTExOWFlZmU2YWUxOTEyY2E2ZTJiMDk2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2018-09-21 04:16:22.386000');
INSERT INTO `django_session` VALUES ('3kptnpsmhbnwonxb7l87v29bo4doznmq', 'MDk0NmM0NWI3YzYxOGY2MTllMmY4NWI1ODZmOWI5MDQxZDQ1MThlYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiR0VUX1BBUkFNIjp7fSwiX2F1dGhfdXNlcl9oYXNoIjoiYzZlZTM1ZjA5ZmE5NzU1NThkNGM4ZThjZTYwNzAwZDNhODdkZjA1ZiIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-09-20 04:50:10.790000');
INSERT INTO `django_session` VALUES ('61gtfa5we3nippm2xg2xurnke2z6n9d6', 'YjE1M2ZmZTc4MDFiYzMzZjhkZjk2NWJmYTYzMTEyYWZkOTI5MzJiMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjdjNTAwYWYyZDg5Y2NhYmYwMGU1OTM4MmUzYzRkYWEyNTUzZTRiMjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-09-19 09:15:06.619000');
INSERT INTO `django_session` VALUES ('aj2ro3jhflrt0xoqzgu6skrnh4v240qr', 'MDk0NmM0NWI3YzYxOGY2MTllMmY4NWI1ODZmOWI5MDQxZDQ1MThlYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiR0VUX1BBUkFNIjp7fSwiX2F1dGhfdXNlcl9oYXNoIjoiYzZlZTM1ZjA5ZmE5NzU1NThkNGM4ZThjZTYwNzAwZDNhODdkZjA1ZiIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-10-07 10:57:48.375000');
INSERT INTO `django_session` VALUES ('dlmghft6ib4sp3j7typgp30ykvzi8dg7', 'MmNlYjM3NDE4Y2MwNjkyOGY3ZTRiNTAzZjUyOTY5YzMyMzYzNmQ2Njp7Il9hdXRoX3VzZXJfaGFzaCI6IjhiNDliNGVlMjFkNGI2NTZhMTE5YWVmZTZhZTE5MTJjYTZlMmIwOTYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-09-21 10:25:51.122000');
INSERT INTO `django_session` VALUES ('hte8tn33cnlu9k10a5pqh6vl049ezasg', 'NmQ5OGE2ZDFmMDc0NmI1OWU2MmNiNGU3NmFkMzlkMjJmOTJkY2ZmYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjdjNTAwYWYyZDg5Y2NhYmYwMGU1OTM4MmUzYzRkYWEyNTUzZTRiMjYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-09-18 23:22:38.745000');
INSERT INTO `django_session` VALUES ('lvgb4yqokwi1jmhzx5yu58ohvcv6i43c', 'NmQ5OGE2ZDFmMDc0NmI1OWU2MmNiNGU3NmFkMzlkMjJmOTJkY2ZmYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjdjNTAwYWYyZDg5Y2NhYmYwMGU1OTM4MmUzYzRkYWEyNTUzZTRiMjYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-09-19 07:24:48.926000');
INSERT INTO `django_session` VALUES ('qdhopikoqy7ubgy0h9ucm8h56hwev2p2', 'MDk0NmM0NWI3YzYxOGY2MTllMmY4NWI1ODZmOWI5MDQxZDQ1MThlYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiR0VUX1BBUkFNIjp7fSwiX2F1dGhfdXNlcl9oYXNoIjoiYzZlZTM1ZjA5ZmE5NzU1NThkNGM4ZThjZTYwNzAwZDNhODdkZjA1ZiIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-09-25 09:40:13.575000');
INSERT INTO `django_session` VALUES ('rmhdj3nrpodaxd6izuqiyfnooswd63im', 'M2FlOGNmMzdlZGQ0Y2MyOWQ1MzcyZGIyNmU0OTk2ZTU2OGZkYjE4MTp7Il9hdXRoX3VzZXJfaGFzaCI6IjhiNDliNGVlMjFkNGI2NTZhMTE5YWVmZTZhZTE5MTJjYTZlMmIwOTYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-10-01 05:55:06.795000');
INSERT INTO `django_session` VALUES ('vga4vizpoyq7854ea7hpp5ydd1772fp5', 'YjE1M2ZmZTc4MDFiYzMzZjhkZjk2NWJmYTYzMTEyYWZkOTI5MzJiMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjdjNTAwYWYyZDg5Y2NhYmYwMGU1OTM4MmUzYzRkYWEyNTUzZTRiMjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-09-17 02:20:07.370000');
INSERT INTO `django_session` VALUES ('vy54d45xe20hc52pyowvw0bstm05pk6z', 'NjRhOTYzMjk3NzAwZTU2MDY0ZThjYmQ1ZGRhNjcyNTA3N2Q3YzBhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZWUzNWYwOWZhOTc1NTU4ZDRjOGU4Y2U2MDcwMGQzYTg3ZGYwNWYiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-10-07 10:36:39.645000');
INSERT INTO `django_session` VALUES ('wca24ucf6gvdwg2gj6k9htumkqk30hjl', 'ODU0MGUxMThmNjAwYzc5NjBhZmNmZGNkYzg5OWVjYWUyNjNmZmIzZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjdiYWEzYTZkYzMzMDlmOGI5NjA2ZjhlNzhlMmE0ZGNkZDJkMjQ4MmIiLCJfYXV0aF91c2VyX2lkIjoiMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-09-18 09:05:34.150000');
INSERT INTO `django_session` VALUES ('wy0qcdwdht656coliyw9ffelvfzvthrb', 'NjRhOTYzMjk3NzAwZTU2MDY0ZThjYmQ1ZGRhNjcyNTA3N2Q3YzBhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZWUzNWYwOWZhOTc1NTU4ZDRjOGU4Y2U2MDcwMGQzYTg3ZGYwNWYiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-09-20 09:38:31.849000');

-- ----------------------------
-- Table structure for happymanagement_happylevel
-- ----------------------------
DROP TABLE IF EXISTS `happymanagement_happylevel`;
CREATE TABLE `happymanagement_happylevel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  `personal_happy_level` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `project_happy_level` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `HappyManagement_happylevel_project_id_3b127878_fk_Sys_project_id` (`project_id`),
  KEY `HappyManagement_happ_create_user_id_ed2330f2_fk_auth_user` (`create_user_id`),
  CONSTRAINT `HappyManagement_happ_create_user_id_ed2330f2_fk_auth_user` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `HappyManagement_happylevel_project_id_3b127878_fk_Sys_project_id` FOREIGN KEY (`project_id`) REFERENCES `sys_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of happymanagement_happylevel
-- ----------------------------
INSERT INTO `happymanagement_happylevel` VALUES ('1', '2018-09-06 09:25:04.810000', '2018-09-06 09:25:04.810000', null, null, null, null, null);
INSERT INTO `happymanagement_happylevel` VALUES ('2', '2018-09-06 09:25:26.305000', '2018-09-06 09:25:26.305000', null, '1', '2', null, null);
INSERT INTO `happymanagement_happylevel` VALUES ('3', '2018-09-06 09:26:25.298000', '2018-09-06 09:26:25.298000', null, null, null, null, null);
INSERT INTO `happymanagement_happylevel` VALUES ('4', '2018-09-06 09:29:52.985000', '2018-09-06 09:29:52.985000', null, null, null, null, null);
INSERT INTO `happymanagement_happylevel` VALUES ('5', '2018-09-06 09:30:59.811000', '2018-09-06 09:30:59.811000', null, null, null, null, null);
INSERT INTO `happymanagement_happylevel` VALUES ('6', '2018-09-06 09:37:22.388000', '2018-09-06 09:37:22.388000', null, null, null, null, null);
INSERT INTO `happymanagement_happylevel` VALUES ('7', '2018-09-06 09:38:31.834000', '2018-09-07 00:36:10.355000', '2', '2', '3', null, '3');
INSERT INTO `happymanagement_happylevel` VALUES ('8', '2018-09-07 00:14:02.751000', '2018-09-07 00:51:50.263000', '2', '2', '2', null, '3');
INSERT INTO `happymanagement_happylevel` VALUES ('9', '2018-09-07 01:01:09.100000', '2018-09-07 01:01:09.100000', '2', '3', '3', '2', '3');
INSERT INTO `happymanagement_happylevel` VALUES ('10', '2018-09-07 01:01:14.175000', '2018-09-07 01:01:14.175000', '2', '2', '2', '2', '3');
INSERT INTO `happymanagement_happylevel` VALUES ('11', '2018-09-07 01:01:18.987000', '2018-09-07 01:01:18.987000', '2', '1', '1', '2', '3');
INSERT INTO `happymanagement_happylevel` VALUES ('12', '2018-09-11 10:57:02.766000', '2018-09-11 10:57:02.766000', '3', '2', '3', '3', '2');
INSERT INTO `happymanagement_happylevel` VALUES ('13', '2018-09-11 11:05:02.936000', '2018-09-11 11:05:02.936000', '3', '2', '2', '3', '2');
INSERT INTO `happymanagement_happylevel` VALUES ('14', '2018-09-11 11:07:50.011000', '2018-09-11 11:07:50.011000', '3', '3', '3', '3', '2');
INSERT INTO `happymanagement_happylevel` VALUES ('15', '2018-09-11 11:09:27.486000', '2018-09-11 11:09:27.486000', '2', '2', '2', '2', '3');
INSERT INTO `happymanagement_happylevel` VALUES ('16', '2018-09-11 23:47:26.866000', '2018-09-11 23:47:26.866000', '2', '2', '3', '2', '3');
INSERT INTO `happymanagement_happylevel` VALUES ('17', '2018-09-11 23:54:37.289000', '2018-09-11 23:54:37.289000', '3', '3', '3', '3', '2');
INSERT INTO `happymanagement_happylevel` VALUES ('18', '2018-09-12 01:43:06.607000', '2018-09-12 01:43:06.607000', '2', '3', '3', '2', '3');
INSERT INTO `happymanagement_happylevel` VALUES ('19', '2018-09-19 06:54:07.266000', '2018-09-19 06:54:07.266000', '3', '3', '3', '3', '2');
INSERT INTO `happymanagement_happylevel` VALUES ('20', '2018-09-19 07:25:56.179000', '2018-09-19 07:25:56.179000', '3', '3', '3', '3', '2');
INSERT INTO `happymanagement_happylevel` VALUES ('21', '2018-09-19 07:29:14.033000', '2018-09-19 07:29:14.033000', '3', '2', '2', '3', '2');

-- ----------------------------
-- Table structure for happymanagement_taskbatch
-- ----------------------------
DROP TABLE IF EXISTS `happymanagement_taskbatch`;
CREATE TABLE `happymanagement_taskbatch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of happymanagement_taskbatch
-- ----------------------------
INSERT INTO `happymanagement_taskbatch` VALUES ('1', '2018-09-09 05:27:32.814000');
INSERT INTO `happymanagement_taskbatch` VALUES ('2', '2018-09-09 05:32:32.823000');
INSERT INTO `happymanagement_taskbatch` VALUES ('3', '2018-09-10 04:07:51.793000');
INSERT INTO `happymanagement_taskbatch` VALUES ('4', '2018-09-10 04:41:14.220000');
INSERT INTO `happymanagement_taskbatch` VALUES ('5', '2018-09-10 04:43:31.577000');
INSERT INTO `happymanagement_taskbatch` VALUES ('6', '2018-09-10 04:52:32.709000');
INSERT INTO `happymanagement_taskbatch` VALUES ('7', '2018-09-10 05:14:39.830000');
INSERT INTO `happymanagement_taskbatch` VALUES ('10', '2018-09-10 05:19:26.352000');
INSERT INTO `happymanagement_taskbatch` VALUES ('11', '2018-09-10 08:34:30.361000');
INSERT INTO `happymanagement_taskbatch` VALUES ('12', '2018-09-10 08:51:23.908000');
INSERT INTO `happymanagement_taskbatch` VALUES ('13', '2018-09-10 08:52:16.541000');
INSERT INTO `happymanagement_taskbatch` VALUES ('14', '2018-09-10 09:03:57.457000');
INSERT INTO `happymanagement_taskbatch` VALUES ('15', '2018-09-10 09:05:04.453000');
INSERT INTO `happymanagement_taskbatch` VALUES ('16', '2018-09-10 09:05:25.333000');
INSERT INTO `happymanagement_taskbatch` VALUES ('17', '2018-09-10 09:05:40.100000');
INSERT INTO `happymanagement_taskbatch` VALUES ('18', '2018-09-10 09:07:13.265000');
INSERT INTO `happymanagement_taskbatch` VALUES ('19', '2018-09-10 09:07:34.378000');
INSERT INTO `happymanagement_taskbatch` VALUES ('20', '2018-09-10 09:07:39.588000');
INSERT INTO `happymanagement_taskbatch` VALUES ('21', '2018-09-10 09:07:52.032000');
INSERT INTO `happymanagement_taskbatch` VALUES ('22', '2018-09-10 09:12:54.562000');
INSERT INTO `happymanagement_taskbatch` VALUES ('23', '2018-09-11 23:12:50.409000');
INSERT INTO `happymanagement_taskbatch` VALUES ('24', '2018-09-12 01:40:52.948000');

-- ----------------------------
-- Table structure for happymanagement_taskstate
-- ----------------------------
DROP TABLE IF EXISTS `happymanagement_taskstate`;
CREATE TABLE `happymanagement_taskstate` (
  `id` char(32) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `task_state` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `task_batch_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of happymanagement_taskstate
-- ----------------------------
INSERT INTO `happymanagement_taskstate` VALUES ('05c82395ce5f45d2a442d2465a2e6206', '', '1', '2', '24', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('084b4340eb0a42c88e956d397609587a', 'x1980p@gmail.com', '3', '3', '15', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('09d30493e61045fb970a5694831f603d', 'x1980p@gmail.com', '3', '3', '10', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('150396ad68784b9d8387df57a7800062', 'x1980p@gmail.com', '3', '3', '17', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('19ed46d7693f44c78b9f5a6904882afa', 'x1980p@gmail.com', '3', '3', '21', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('1cf47e715c7d478b9d73d3acaf3f805a', 'x1980p@gmail.com', '3', '3', '3', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('2ed0a528eba64b4c933a09760ad9386f', 'x1980p@gmail.com', '3', '3', '2', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('32939fa14ce044dfa0594b44c1d48b19', 'x1980p@gmail.com', '3', '3', '11', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('420eca8c02574cf6a452ad78200c667f', '', '3', '2', '17', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('47d4ddc15da2427bbc64ebb1c923d6c4', '', '2', '2', '1', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('4ec107542f0c49fa948f3f0a972c63ce', 'x1980p@gmail.com', '2', '3', '23', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('5e1e29f2417e459cbc27636be45c2e29', '', '3', '2', '12', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('5f16337f351a4337b69b62f034e138d9', 'x1980p@gmail.com', '3', '3', '14', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('6b9ac331c8d64bd3ae86b23a2626135c', '', '3', '2', '19', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('73b28716edae48628068fef94e7b7fe4', '', '3', '2', '16', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('7435f5fb83884152af881b9e601c5ac9', '', '2', '2', '23', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('801274f0be3140749d0b8f5a91f4ba7b', '', '3', '2', '3', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('810ac8698b7c4ad787edf459e912130d', 'x1980p@gmail.com', '3', '3', '20', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('8821d0bc349d4cf7ab590a331e1fffd0', '', '2', '2', '22', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('89ad537ec2f9437298a6288db5011979', 'x1980p@gmail.com', '3', '3', '5', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('988518798c504e7eb19e506ce44bb775', 'x1980p@gmail.com', '3', '3', '1', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('9cc11794b04a47cda476fd941d745b06', 'x1980p@gmail.com', '3', '3', '6', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('9d004959aac24918b03ce772720f56d8', '', '3', '2', '10', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('ac7e4e24e8bc4826822b85c0f6f2921d', '', '3', '2', '5', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('ad100cd0f04947ed9d960efb0b595ece', '', '3', '2', '14', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('bc7f3f6ad1054efe8e6b9d7872660d9b', '', '3', '2', '7', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('bd2e1f1436124af5b1ba4dc7d09fff2b', '', '3', '2', '2', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('c0e0804af30d4a80b6bac162b6e06bfb', '', '3', '2', '6', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('c38f06ce670c4616a9aea63b2d1d0287', '', '3', '2', '15', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('c4364a8e575d43d49a7997aca4f4ded3', 'x1980p@gmail.com', '2', '3', '22', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('c8f2d02d407e4524969ef57e0668ffc0', 'x1980p@gmail.com', '3', '3', '19', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('c9fa38e07dc541f7a98e82f01b8ad640', 'x1980p@gmail.com', '3', '3', '16', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('caeb4b6320464774969efa21f11a7793', 'x1980p@gmail.com', '3', '3', '7', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('d1d036e83a0f4be1af39db681ee0c47d', 'x1980p@gmail.com', '3', '3', '13', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('d231423979044614aeebceb9423f0e3d', '', '3', '2', '20', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('d36c8f1a83344ea3bc38a0fee05563db', 'x1980p@gmail.com', '2', '3', '24', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('d63ed13709a7495c8c4dcc26f6065680', '', '3', '2', '21', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('d9d6e706ec8f417187066a801a1eecc2', 'x1980p@gmail.com', '3', '3', '12', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('dbe9d3cb994c4bc9932af2e57dcfb897', 'x1980p@gmail.com', '3', '3', '18', '2');
INSERT INTO `happymanagement_taskstate` VALUES ('e0abd41bcdf743e092ebae8328b1b578', '', '3', '2', '11', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('e129d06797da4e2d8473cc0f6628c686', '', '2', '2', '13', '3');
INSERT INTO `happymanagement_taskstate` VALUES ('ecec3b2abcc5497b9e681f7e1f55a0a2', '', '2', '2', '18', '3');

-- ----------------------------
-- Table structure for sys_project
-- ----------------------------
DROP TABLE IF EXISTS `sys_project`;
CREATE TABLE `sys_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectName` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `projectDescribe` longtext COLLATE utf8_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of sys_project
-- ----------------------------
INSERT INTO `sys_project` VALUES ('1', 'porject1', 'project1', '0');
INSERT INTO `sys_project` VALUES ('2', 'project2', 'project2', '1');
INSERT INTO `sys_project` VALUES ('3', 'project3', 'Project3', '1');
