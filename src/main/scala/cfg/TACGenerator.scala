package cfg

import org.opalj.br.analyses.Project
import org.opalj.br.{DeclaredMethod, Method}
import org.opalj.tac._
import org.opalj.value.ValueInformation

import java.io.{File, PrintWriter}
import java.nio.file.Paths
import java.util

case class TACGenerator(tacMap: Map[DeclaredMethod, Option[AITACode[TACMethodParameter, ValueInformation]]]) {
  type TAC = AITACode[TACMethodParameter, ValueInformation]

  def printToFile[T](directory: File): Unit = {
    val groupedMap = tacMap.keySet.groupBy(_.declaringClassType)
    val dir = new File(Paths.get(directory.getAbsolutePath, "tac").toString)
    if (!dir.exists) {
      dir.mkdir()
    }
    for (obj <- groupedMap.keys) {
      val pw =
        if (Paths.get(dir.getAbsolutePath, obj.toJava + ".tac").toString.length > 200)
          new PrintWriter(new File(Paths.get(dir.getAbsolutePath, obj.toJava.substring(0, 196 - dir.getAbsolutePath.length) + ".tac").toString))
        else
          new PrintWriter(new File(Paths.get(dir.getAbsolutePath, obj.toJava + ".tac").toString))
      for (method <- groupedMap(obj)) {
        tacMap(method) match {
          case Some(value) => pw.write(method.descriptor.toJava(method.name) + "\n"); pw.write(value.toString() + "\n\n")
          case None => pw.write(method.name + "\n\n");
        }
      }
      pw.close()
    }
  }

  def get(method: DeclaredMethod): Option[TAC] = tacMap(method)

  def get(method: Method): TAC = {
    val opt = tacMap.filter(k => k._1.hasSingleDefinedMethod && k._1.definedMethod.equals(method) && k._1.definedMethod.body.isDefined).map(a => (a._1.definedMethod, a._2.get)).get(method)
    if (opt.isEmpty) {
      //println(method)
      //println(method.body)
    }
    try {
      tacMap.filter(k => k._1.hasSingleDefinedMethod && k._1.definedMethod.equals(method)).map(a => (a._1.definedMethod, a._2.get)).get(method).get
    }
    catch {
      case a => println("ALSJKDASL"); println(method); println(opt); println(tacMap); throw a
    }
  }
}

object TACGenerator {
  def apply[T](methods: Iterable[DeclaredMethod])(implicit p: Project[T]): TACGenerator = {
    //    if (!methods.foldLeft(true)((a, m) => a && m.hasSingleDefinedMethod)) {
    //      println(methods.filter(!_.hasSingleDefinedMethod))
    //      throw RuntimeException("Can't handle virtual method or multiple defined method yet")
    //    }
    val tac = p.get(ComputeTACAIKey)
    TACGenerator(methods.map(m => (m, if (m.hasSingleDefinedMethod && m.definedMethod.body.isDefined) Some(tac(m.definedMethod)) else None)).toMap)
  }
}
