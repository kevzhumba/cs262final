package cli

import java.io.File

case class Config(
                   project: File = new File("."),
                   interact: Boolean = false,
                   generate_tac: Boolean = false,
                   heap: Boolean = false,
                   out: File = new File("."),
                   worker: Boolean = false,
                   host: String = "",
                   port: Int = 0,
                   machines: List[(String, Int)] = List()
                 )