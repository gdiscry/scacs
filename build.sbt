name := "Scala Cluster Service"

normalizedName := "scacs"

version := "0.1-SNAPSHOT"

resolvers += "Typesafe Repository" at "http://repo.typesafe.com/typesafe/releases/" 

libraryDependencies += "com.typesafe.akka" % "akka-actor" % "2.0"
 
libraryDependencies += "com.typesafe.akka" % "akka-remote" % "2.0"
