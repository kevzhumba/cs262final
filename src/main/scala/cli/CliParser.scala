package cli

import scopt.OParser

import java.io.File

object CliParser {
  val builder = OParser.builder[Config]
  val parser = {
    import builder._
    OParser.sequence(
      programName("PathSensitiveFramework"),
      head("psf", "0.1"),
      arg[File]("<file>")
        .action((x, c) => c.copy(project=x))
        .text("path to java project"),
      opt[Unit]('i', "interact")
        .action((i, c) => c.copy(interact = true))
        .text("interactive mode"),
      opt[Unit]('g', "generate-tac")
        .action((g, c) => c.copy(generate_tac = true))
        .text("generate and save tac"),
      opt[File]('o', "out")
        .action((o, c) => c.copy(out = o))
        .text("output directory"),
      opt[Unit]('w', "worker")
        .action((w, c) => c.copy(worker =  true))
        .text("worker machine"),
      opt[Int]('p',"port")
        .action((p, c) => c.copy(port = p))
        .text("port"),
      opt[String]('h', "host")
        .action((h, c) => c.copy(host = h))
        .text("host"),

    )
  }

  def parseArgs(args:Array[String]): Option[Config] =
    OParser.parse(parser, args, Config())

}
