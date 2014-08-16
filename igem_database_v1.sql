-- MySQL dump 10.13  Distrib 5.6.19, for osx10.9 (x86_64)
--
-- Host: localhost    Database: igem1
-- ------------------------------------------------------
-- Server version	5.6.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `igem1`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `igem1` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `igem1`;

--
-- Table structure for table `component`
--

DROP TABLE IF EXISTS `component`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `component` (
  `id` int(11) NOT NULL,
  `name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `component`
--

LOCK TABLES `component` WRITE;
/*!40000 ALTER TABLE `component` DISABLE KEYS */;
/*!40000 ALTER TABLE `component` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `intermediate`
--

DROP TABLE IF EXISTS `intermediate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `intermediate` (
  `id` int(11) NOT NULL,
  `name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intermediate`
--

LOCK TABLES `intermediate` WRITE;
/*!40000 ALTER TABLE `intermediate` DISABLE KEYS */;
/*!40000 ALTER TABLE `intermediate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operon_component`
--

DROP TABLE IF EXISTS `operon_component`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operon_component` (
  `id` int(11) NOT NULL,
  `operon_id` int(11) DEFAULT NULL,
  `component_id` int(11) DEFAULT NULL,
  `position` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operon_component`
--

LOCK TABLES `operon_component` WRITE;
/*!40000 ALTER TABLE `operon_component` DISABLE KEYS */;
/*!40000 ALTER TABLE `operon_component` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operon_input`
--

DROP TABLE IF EXISTS `operon_input`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operon_input` (
  `id` int(11) NOT NULL,
  `operon_id` int(11) DEFAULT NULL,
  `input` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operon_input`
--

LOCK TABLES `operon_input` WRITE;
/*!40000 ALTER TABLE `operon_input` DISABLE KEYS */;
/*!40000 ALTER TABLE `operon_input` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operon_math`
--

DROP TABLE IF EXISTS `operon_math`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operon_math` (
  `id` int(11) NOT NULL,
  `operon_id` int(11) DEFAULT NULL,
  `math` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operon_math`
--

LOCK TABLES `operon_math` WRITE;
/*!40000 ALTER TABLE `operon_math` DISABLE KEYS */;
/*!40000 ALTER TABLE `operon_math` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operon_output`
--

DROP TABLE IF EXISTS `operon_output`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operon_output` (
  `id` int(11) NOT NULL,
  `operon_id` int(11) DEFAULT NULL,
  `output` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operon_output`
--

LOCK TABLES `operon_output` WRITE;
/*!40000 ALTER TABLE `operon_output` DISABLE KEYS */;
/*!40000 ALTER TABLE `operon_output` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operon_plasmid`
--

DROP TABLE IF EXISTS `operon_plasmid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operon_plasmid` (
  `id` int(11) NOT NULL,
  `operon_id` int(11) DEFAULT NULL,
  `plasmid_id` int(11) DEFAULT NULL,
  `main` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operon_plasmid`
--

LOCK TABLES `operon_plasmid` WRITE;
/*!40000 ALTER TABLE `operon_plasmid` DISABLE KEYS */;
/*!40000 ALTER TABLE `operon_plasmid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plasmid`
--

DROP TABLE IF EXISTS `plasmid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plasmid` (
  `id` int(11) NOT NULL,
  `name` text,
  `size` int(11) DEFAULT NULL,
  `m_id` int(11) DEFAULT NULL,
  `image_path` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plasmid`
--

LOCK TABLES `plasmid` WRITE;
/*!40000 ALTER TABLE `plasmid` DISABLE KEYS */;
/*!40000 ALTER TABLE `plasmid` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-08-08 19:43:44
