val scala3Version = "2.13.10"
//ThisBuild / assemblyMergeStrategy := {
//  case PathList("module-info.class") => MergeStrategy.discard
//  case x =>
//    val oldStrategy = (ThisBuild / assemblyMergeStrategy).value
//    oldStrategy(x)
//}
testOptions in Test += Tests.Argument("-oF")

Test / parallelExecution := false

Compile / PB.targets := Seq(
  scalapb.gen() -> (Compile / sourceManaged).value / "scalapb"
)
lazy val root = project
  .in(file("."))
  .settings(
    name := "cs262final",
    version := "0.1.0-SNAPSHOT",
    resolvers += "scala-integration" at "https://scala-ci.typesafe.com/artifactory/scala-integration/",
    scalaVersion := scala3Version,
    libraryDependencies += "org.scalameta" %% "munit" % "0.7.29" % Test,
    libraryDependencies += ("de.opal-project" %% "framework" % "5.0.0"),
    libraryDependencies += "com.github.scopt" %% "scopt" % "4.1.0",
    libraryDependencies ++= Seq(
      "io.grpc" % "grpc-netty" % scalapb.compiler.Version.grpcJavaVersion,
      "com.thesamet.scalapb" %% "scalapb-runtime-grpc" % scalapb.compiler.Version.scalapbVersion
    ),
    libraryDependencies += "org.json4s" %% "json4s-native" % "4.0.6"
  )
