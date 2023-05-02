
import com.typesafe.config.ConfigValueFactory
import org.opalj.ai._
import org.opalj.br._
import org.opalj.br.analyses._
import org.opalj.br.analyses.Project.{JavaClassFileReader, JavaLibraryClassFileReader}
import org.opalj.br.analyses.cg.{AllEntryPointsFinder, InitialEntryPointsKey}
import org.opalj.br.instructions._
import org.opalj.bytecode._
import org.opalj.tac._

import java.io.File
import java.net.URL
import java.util

object JavaLoader {

  def loadJavaProject(f: File): Project[URL] = {
    implicit val config = BaseConfig.withValue(
      InitialEntryPointsKey.ConfigKey, ConfigValueFactory.fromAnyRef(
        "org.opalj.br.analyses.cg.ApplicationWithoutJREEntryPointsFinder"
      )).withValue(
      AllEntryPointsFinder.ConfigKey, ConfigValueFactory.fromAnyRef(true)
    ).withValue(InitialEntryPointsKey.ConfigKeyPrefix + "entryPoints", ConfigValueFactory.fromAnyRef(new util.ArrayList[String]()))
    val p = Project(JavaClassFileReader().ClassFiles(f) ++ JavaClassFileReader().ClassFiles(RTJar), Iterable.empty, libraryClassFilesAreInterfacesOnly = false, Iterable.empty)
    p
  }


}
