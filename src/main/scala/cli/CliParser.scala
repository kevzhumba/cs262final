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
        .required()
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
      opt[Unit]('h', "heap")
        .action((h, c) => c.copy(heap = true))
        .text("print heap")
    )
  }

  def parseArgs(args:Array[String]): Option[Config] =
    OParser.parse(parser, args, Config())

}
