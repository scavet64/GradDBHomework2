SET FOREIGN_KEY_CHECKS=0;
drop table IF EXISTS `category`;
drop table IF EXISTS `customer`;
drop table IF EXISTS `customer_wishlist`;
drop table IF EXISTS `product`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email_address` varchar(45) NOT NULL,
  `last_login` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8

CREATE TABLE `customer_wishlist` (
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`customer_id`,`product_id`),
  KEY `FK_customer_wishlist_idx` (`customer_id`),
  KEY `FK_product_wishlist_idx` (`product_id`),
  CONSTRAINT `FK_customer_wishlist` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_product_wishlist` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  `supplier_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `cost` double NOT NULL,
  `reorder_level` int(11) NOT NULL,
  `weight_unit_of_measure` varchar(45) NOT NULL,
  `weight` double NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `FK_product_category_idx` (`category_id`),
  CONSTRAINT `FK_product_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8

insert into 