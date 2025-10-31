-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: devops_chatbot
-- ------------------------------------------------------
-- Server version	5.5.5-10.8.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `devops_issues`
--

DROP TABLE IF EXISTS `devops_issues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `devops_issues` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `failure` varchar(3000) NOT NULL,
  `root_cause` varchar(1000) NOT NULL,
  `solution` varchar(2000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devops_issues`
--

LOCK TABLES `devops_issues` WRITE;
/*!40000 ALTER TABLE `devops_issues` DISABLE KEYS */;
INSERT INTO `devops_issues` VALUES (1,'ERROR :: Command(git am <path>/6715314649237516733_patch/*.patch --keep-cr --3way) failed after maximum retry ... script returned exit code 255','Git patch application failure due to merge conflicts or corrupted patches. The git am command with 3-way merge strategy exhausted retry attempts.','If there are merge conflicts during git am --3way, rebase your workspace, resolve conflicts if any. Afterwards push the changes and retrigger.'),(2,'Unable to find image \'docker.io/library/hello-world:latest\' locally\ndocker: Error response from daemon: pull access denied for hello-world, repository does not exist or may require \'docker login\'.','This error occurs because Docker couldn\'t pull the image from the private registry due to network timeout, connectivity issues, missing permissions, or an invalid image/tag.','First check manual docker pull from artifactory. If manual pull also fails, check for the same image and tag in artifactory to verify if it exists. '),(3,'{\'Commit issue (Dev)\': \'Dynamic Code Coverage Threshold(70%) not met\', \'Environment issue\': []} INFO :: Environment variables :: {\'FAIL_CATEGORY\': \'Commit issue (Dev)\', \'FAIL_REASON\': \'Dynamic Code Coverage Threshold(70%) not met\'} script returned exit code 1','Dynamic Code Coverage Threshold(70%) not is met and minimum requirement set for dynamic code coverage is 70 percent.','Kindly maintain the minimum coverage and write necessary testcase to increase the coverage.'),(4,'Failure: Stage failed due to error: hudson.AbortException: script returned exit code 1','This error indicates that script or command within your pipeline stage executed and failed. Jenkins throws this exception when a build step fails. It\'s Jenkins\' way of saying \"something went wrong and we\'re stopping the build\"','Examine the console logs. The key is to look at the console output right before this error to see what specific command or script actually failed!'),(5,'Branch not set issue in pool git status HEAD detached from FETCH_HEAD Untracked files: nothing added to commit but untracked files present (use \"git add\" to track)','Head detached from master.','checkout to your branch <your_branch> and then retrigger pool mt.'),(6,'Jenkins Build Timeout','Jenkins build timing out during execution phase','1. Increase build timeout 2. Optimize build steps 3. Check system resources'),(7,'Kubernetes Pod CrashLoopBackOff','Pod continuously crashes and restarts in Kubernetes cluster','1. Check pod logs kubectl logs pod-name 2. Verify resource limits 3. Check probes'),(8,'Jenkins Build Timeout','Jenkins build timing out during execution phase','1. Increase build timeout 2. Optimize build steps 3. Check system resources'),(9,'GitLab CI Pipeline Failure - Dependency Issues','Pipeline fails due to missing or incompatible dependencies','1. Update dependency versions 2. Clear pipeline cache 3. Check lock files'),(10,'Deployment Rollback Required','Production deployment causing issues requiring immediate rollback','1. Identify failed deployment 2. Execute rollback 3. Verify service health');
/*!40000 ALTER TABLE `devops_issues` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-31 17:49:49
