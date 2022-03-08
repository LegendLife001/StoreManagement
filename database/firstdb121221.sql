-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: store
-- ------------------------------------------------------
-- Server version	8.0.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Product_Name` varchar(100) NOT NULL,
  `stock` int NOT NULL,
  `cp` int DEFAULT NULL,
  `sp` int DEFAULT NULL,
  `totalcp` int DEFAULT NULL,
  `totalsp` int DEFAULT NULL,
  `assumed_profit` int DEFAULT NULL,
  `Vender` varchar(100) DEFAULT NULL,
  `date` varchar(12) DEFAULT NULL,
  `time` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'Octance_Pen',100,7,10,700,1000,300,'Classmate','29.11.2021','11:00:00'),(2,'KitKat',100,20,25,2000,2500,500,'Nestle','29.11.2021','11:00:00'),(3,'Pen Drive',50,450,520,22500,26000,3500,'SONY','29.11.2021','11:00:00'),(4,'Boltt BH1400_headphone',30,1300,1500,39000,45000,6000,'BOLTT','29.11.2021','11:00:00'),(5,'Mighty Bottle 750mL',50,80,100,4000,5000,1000,'Mighty','29.11.2021','11:00:00'),(6,'Surgical Mask',120,4,5,480,600,120,'xyz','29.11.2021','11:00:00'),(7,'N95 Mask',100,40,45,4000,4500,500,'SWASA','29.11.2021','11:00:00'),(8,'Lays_HotnSweetChilli',60,17,20,1020,1200,180,'lays','29.11.2021','11:00:00'),(9,'Battey-AAA',48,8,10,400,500,100,'EVERYDAY','29.11.2021','11:00:00'),(10,'Notebook_24x18',40,45,50,2250,2500,250,'Classmate','29.11.2021','11:00:00'),(11,'Apsara_Plt_pencil',50,44,50,2200,2500,300,'Apsara','29.11.2021','11:00:00'),(12,'DairyMilk_nuts',50,70,80,3500,4000,500,'Cadbury','29.11.2021','11:00:00'),(13,'adidas_shoe',25,500,600,12500,15000,2500,'Adidas','29.11.2021','11:00:00'),(14,'Lays_cream&onion',48,17,20,850,1000,150,'Lays','29.11.2021','11:00:00'),(15,'lock_6lvl',25,40,50,1000,1250,250,'Godrej','29.11.2021','11:00:00'),(16,'powerbank_20000',30,1300,1500,39000,45000,6000,'Coolnut','29.11.2021','11:00:00'),(17,'SSD_1tb',30,9000,12000,270000,360000,90000,'Sandisk','29.11.2021','11:00:00'),(18,'stapler ',50,40,50,2000,2500,500,'Kangaro','29.11.2021','11:00:00'),(19,'school_bag',50,600,800,30000,40000,10000,'Skybags','29.11.2021','11:00:00'),(20,'Ruler_30',34,13,15,455,525,70,'Khyati','29.11.2021','11:00:00'),(21,'paper_weight',30,170,200,5100,6000,900,'Godrej','29.11.2021','11:00:00'),(22,'leatherJacket',25,5000,6000,125000,150000,25000,'Cobb','29.11.2021','11:00:00'),(23,'HDD_2tb',30,5000,7000,150000,210000,60000,'Seagate','29.11.2021','11:00:00'),(24,'card_reader',39,130,150,5200,6000,800,'Enter','29.11.2021','11:00:00'),(25,'cadbury_silk',90,60,80,6000,8000,2000,'Cadbury','29.11.2021','12:10:04'),(26,'lead_pencil',35,25,30,875,1050,175,'Camlin','29.11.2021','12:22:16'),(27,'ClassXII_bookset',20,550,600,16500,18000,1500,'NCERT','30.11.2021','12:11:15'),(28,'Liquid_handwash',50,90,100,4500,5000,500,'Dettol','30.11.2021','15:05:11'),(29,'360_ruler',30,22,25,660,750,90,'Maped','07.12.2021','17:52:10'),(30,'marker_pen',30,18,20,540,600,60,'Camlin','07.12.2021','17:52:33'),(31,'physics_notes',50,80,100,4000,5000,1000,'physics','07.12.2021','17:53:36'),(32,'mosquito_bat',20,90,100,1800,2000,200,'Onlite','07.12.2021','22:40:45'),(33,'tennis_ball',49,28,30,1400,1500,100,'Sg','08.12.2021','10:13:06'),(34,'Home_Cusion',30,90,100,2700,3000,300,'Homie','08.12.2021','14:42:17'),(35,'usbC_cable',30,270,300,8100,9000,900,'Samsung','08.12.2021','14:42:55'),(36,'body_lotion121',50,460,500,23000,25000,2000,'Nivea','08.12.2021','14:43:49'),(37,'newspaper',100,3,4,300,400,100,'Indian_Express','08.12.2021','14:44:24');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `ID` int DEFAULT NULL,
  `Product_Name` varchar(100) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Received_Amount` int DEFAULT NULL,
  `date` varchar(12) DEFAULT NULL,
  `time` varchar(12) DEFAULT NULL,
  `invoice` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (9,'Battey-AAA',2,20,'12.12.2021','11:18:08',1004),(20,'Ruler_30',1,15,'12.12.2021','11:18:08',1004),(24,'card_reader',1,150,'12.12.2021','11:18:08',1004),(14,'Lays_cream&onion',2,40,'12.12.2021','11:18:08',1004);
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-12 12:01:14
