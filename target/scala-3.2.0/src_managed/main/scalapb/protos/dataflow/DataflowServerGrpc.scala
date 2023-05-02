// Generated by the Scala Plugin for the Protocol Buffer Compiler.
// Do not edit!
//
// Protofile syntax: PROTO3

package protos.dataflow


object DataflowServerGrpc {
  val METHOD_GET_CALLER_INFO: _root_.io.grpc.MethodDescriptor[protos.dataflow.GetCallerInfoRequest, protos.dataflow.GetCallerInfoResponse] =
    _root_.io.grpc.MethodDescriptor.newBuilder()
      .setType(_root_.io.grpc.MethodDescriptor.MethodType.UNARY)
      .setFullMethodName(_root_.io.grpc.MethodDescriptor.generateFullMethodName("protos.DataflowServer", "GetCallerInfo"))
      .setSampledToLocalTracing(true)
      .setRequestMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.GetCallerInfoRequest])
      .setResponseMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.GetCallerInfoResponse])
      .setSchemaDescriptor(_root_.scalapb.grpc.ConcreteProtoMethodDescriptorSupplier.fromMethodDescriptor(protos.dataflow.DataflowProto.javaDescriptor.getServices().get(0).getMethods().get(0)))
      .build()
  
  val METHOD_GET_CALLEE_INFO: _root_.io.grpc.MethodDescriptor[protos.dataflow.GetCalleeInfoRequest, protos.dataflow.GetCalleeInfoResponse] =
    _root_.io.grpc.MethodDescriptor.newBuilder()
      .setType(_root_.io.grpc.MethodDescriptor.MethodType.UNARY)
      .setFullMethodName(_root_.io.grpc.MethodDescriptor.generateFullMethodName("protos.DataflowServer", "GetCalleeInfo"))
      .setSampledToLocalTracing(true)
      .setRequestMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.GetCalleeInfoRequest])
      .setResponseMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.GetCalleeInfoResponse])
      .setSchemaDescriptor(_root_.scalapb.grpc.ConcreteProtoMethodDescriptorSupplier.fromMethodDescriptor(protos.dataflow.DataflowProto.javaDescriptor.getServices().get(0).getMethods().get(1)))
      .build()
  
  val METHOD_GET_HEARTBEAT: _root_.io.grpc.MethodDescriptor[protos.dataflow.GetHeartbeatRequest, protos.dataflow.GetHeartbeatResponse] =
    _root_.io.grpc.MethodDescriptor.newBuilder()
      .setType(_root_.io.grpc.MethodDescriptor.MethodType.UNARY)
      .setFullMethodName(_root_.io.grpc.MethodDescriptor.generateFullMethodName("protos.DataflowServer", "GetHeartbeat"))
      .setSampledToLocalTracing(true)
      .setRequestMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.GetHeartbeatRequest])
      .setResponseMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.GetHeartbeatResponse])
      .setSchemaDescriptor(_root_.scalapb.grpc.ConcreteProtoMethodDescriptorSupplier.fromMethodDescriptor(protos.dataflow.DataflowProto.javaDescriptor.getServices().get(0).getMethods().get(2)))
      .build()
  
  val METHOD_RECEIVE_COMPUTATION_UNIT: _root_.io.grpc.MethodDescriptor[protos.dataflow.ReceiveComputationUnitRequest, protos.dataflow.ReceiveComputationUnitResponse] =
    _root_.io.grpc.MethodDescriptor.newBuilder()
      .setType(_root_.io.grpc.MethodDescriptor.MethodType.UNARY)
      .setFullMethodName(_root_.io.grpc.MethodDescriptor.generateFullMethodName("protos.DataflowServer", "ReceiveComputationUnit"))
      .setSampledToLocalTracing(true)
      .setRequestMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.ReceiveComputationUnitRequest])
      .setResponseMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.ReceiveComputationUnitResponse])
      .setSchemaDescriptor(_root_.scalapb.grpc.ConcreteProtoMethodDescriptorSupplier.fromMethodDescriptor(protos.dataflow.DataflowProto.javaDescriptor.getServices().get(0).getMethods().get(3)))
      .build()
  
  val METHOD_SET_TRIGGER: _root_.io.grpc.MethodDescriptor[protos.dataflow.SetTriggerRequest, protos.dataflow.SetTriggerResponse] =
    _root_.io.grpc.MethodDescriptor.newBuilder()
      .setType(_root_.io.grpc.MethodDescriptor.MethodType.UNARY)
      .setFullMethodName(_root_.io.grpc.MethodDescriptor.generateFullMethodName("protos.DataflowServer", "SetTrigger"))
      .setSampledToLocalTracing(true)
      .setRequestMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.SetTriggerRequest])
      .setResponseMarshaller(_root_.scalapb.grpc.Marshaller.forMessage[protos.dataflow.SetTriggerResponse])
      .setSchemaDescriptor(_root_.scalapb.grpc.ConcreteProtoMethodDescriptorSupplier.fromMethodDescriptor(protos.dataflow.DataflowProto.javaDescriptor.getServices().get(0).getMethods().get(4)))
      .build()
  
  val SERVICE: _root_.io.grpc.ServiceDescriptor =
    _root_.io.grpc.ServiceDescriptor.newBuilder("protos.DataflowServer")
      .setSchemaDescriptor(new _root_.scalapb.grpc.ConcreteProtoFileDescriptorSupplier(protos.dataflow.DataflowProto.javaDescriptor))
      .addMethod(METHOD_GET_CALLER_INFO)
      .addMethod(METHOD_GET_CALLEE_INFO)
      .addMethod(METHOD_GET_HEARTBEAT)
      .addMethod(METHOD_RECEIVE_COMPUTATION_UNIT)
      .addMethod(METHOD_SET_TRIGGER)
      .build()
  
  /** The greeting service definition.
    */
  trait DataflowServer extends _root_.scalapb.grpc.AbstractService {
    override def serviceCompanion = DataflowServer
    /** Sends a greeting
      */
    def getCallerInfo(request: protos.dataflow.GetCallerInfoRequest): scala.concurrent.Future[protos.dataflow.GetCallerInfoResponse]
    def getCalleeInfo(request: protos.dataflow.GetCalleeInfoRequest): scala.concurrent.Future[protos.dataflow.GetCalleeInfoResponse]
    def getHeartbeat(request: protos.dataflow.GetHeartbeatRequest): scala.concurrent.Future[protos.dataflow.GetHeartbeatResponse]
    def receiveComputationUnit(request: protos.dataflow.ReceiveComputationUnitRequest): scala.concurrent.Future[protos.dataflow.ReceiveComputationUnitResponse]
    def setTrigger(request: protos.dataflow.SetTriggerRequest): scala.concurrent.Future[protos.dataflow.SetTriggerResponse]
  }
  
  object DataflowServer extends _root_.scalapb.grpc.ServiceCompanion[DataflowServer] {
    implicit def serviceCompanion: _root_.scalapb.grpc.ServiceCompanion[DataflowServer] = this
    def javaDescriptor: _root_.com.google.protobuf.Descriptors.ServiceDescriptor = protos.dataflow.DataflowProto.javaDescriptor.getServices().get(0)
    def scalaDescriptor: _root_.scalapb.descriptors.ServiceDescriptor = protos.dataflow.DataflowProto.scalaDescriptor.services(0)
    def bindService(serviceImpl: DataflowServer, executionContext: scala.concurrent.ExecutionContext): _root_.io.grpc.ServerServiceDefinition =
      _root_.io.grpc.ServerServiceDefinition.builder(SERVICE)
      .addMethod(
        METHOD_GET_CALLER_INFO,
        _root_.io.grpc.stub.ServerCalls.asyncUnaryCall(new _root_.io.grpc.stub.ServerCalls.UnaryMethod[protos.dataflow.GetCallerInfoRequest, protos.dataflow.GetCallerInfoResponse] {
          override def invoke(request: protos.dataflow.GetCallerInfoRequest, observer: _root_.io.grpc.stub.StreamObserver[protos.dataflow.GetCallerInfoResponse]): _root_.scala.Unit =
            serviceImpl.getCallerInfo(request).onComplete(scalapb.grpc.Grpc.completeObserver(observer))(
              executionContext)
        }))
      .addMethod(
        METHOD_GET_CALLEE_INFO,
        _root_.io.grpc.stub.ServerCalls.asyncUnaryCall(new _root_.io.grpc.stub.ServerCalls.UnaryMethod[protos.dataflow.GetCalleeInfoRequest, protos.dataflow.GetCalleeInfoResponse] {
          override def invoke(request: protos.dataflow.GetCalleeInfoRequest, observer: _root_.io.grpc.stub.StreamObserver[protos.dataflow.GetCalleeInfoResponse]): _root_.scala.Unit =
            serviceImpl.getCalleeInfo(request).onComplete(scalapb.grpc.Grpc.completeObserver(observer))(
              executionContext)
        }))
      .addMethod(
        METHOD_GET_HEARTBEAT,
        _root_.io.grpc.stub.ServerCalls.asyncUnaryCall(new _root_.io.grpc.stub.ServerCalls.UnaryMethod[protos.dataflow.GetHeartbeatRequest, protos.dataflow.GetHeartbeatResponse] {
          override def invoke(request: protos.dataflow.GetHeartbeatRequest, observer: _root_.io.grpc.stub.StreamObserver[protos.dataflow.GetHeartbeatResponse]): _root_.scala.Unit =
            serviceImpl.getHeartbeat(request).onComplete(scalapb.grpc.Grpc.completeObserver(observer))(
              executionContext)
        }))
      .addMethod(
        METHOD_RECEIVE_COMPUTATION_UNIT,
        _root_.io.grpc.stub.ServerCalls.asyncUnaryCall(new _root_.io.grpc.stub.ServerCalls.UnaryMethod[protos.dataflow.ReceiveComputationUnitRequest, protos.dataflow.ReceiveComputationUnitResponse] {
          override def invoke(request: protos.dataflow.ReceiveComputationUnitRequest, observer: _root_.io.grpc.stub.StreamObserver[protos.dataflow.ReceiveComputationUnitResponse]): _root_.scala.Unit =
            serviceImpl.receiveComputationUnit(request).onComplete(scalapb.grpc.Grpc.completeObserver(observer))(
              executionContext)
        }))
      .addMethod(
        METHOD_SET_TRIGGER,
        _root_.io.grpc.stub.ServerCalls.asyncUnaryCall(new _root_.io.grpc.stub.ServerCalls.UnaryMethod[protos.dataflow.SetTriggerRequest, protos.dataflow.SetTriggerResponse] {
          override def invoke(request: protos.dataflow.SetTriggerRequest, observer: _root_.io.grpc.stub.StreamObserver[protos.dataflow.SetTriggerResponse]): _root_.scala.Unit =
            serviceImpl.setTrigger(request).onComplete(scalapb.grpc.Grpc.completeObserver(observer))(
              executionContext)
        }))
      .build()
  }
  
  /** The greeting service definition.
    */
  trait DataflowServerBlockingClient {
    def serviceCompanion = DataflowServer
    /** Sends a greeting
      */
    def getCallerInfo(request: protos.dataflow.GetCallerInfoRequest): protos.dataflow.GetCallerInfoResponse
    def getCalleeInfo(request: protos.dataflow.GetCalleeInfoRequest): protos.dataflow.GetCalleeInfoResponse
    def getHeartbeat(request: protos.dataflow.GetHeartbeatRequest): protos.dataflow.GetHeartbeatResponse
    def receiveComputationUnit(request: protos.dataflow.ReceiveComputationUnitRequest): protos.dataflow.ReceiveComputationUnitResponse
    def setTrigger(request: protos.dataflow.SetTriggerRequest): protos.dataflow.SetTriggerResponse
  }
  
  class DataflowServerBlockingStub(channel: _root_.io.grpc.Channel, options: _root_.io.grpc.CallOptions = _root_.io.grpc.CallOptions.DEFAULT) extends _root_.io.grpc.stub.AbstractStub[DataflowServerBlockingStub](channel, options) with DataflowServerBlockingClient {
    /** Sends a greeting
      */
    override def getCallerInfo(request: protos.dataflow.GetCallerInfoRequest): protos.dataflow.GetCallerInfoResponse = {
      _root_.scalapb.grpc.ClientCalls.blockingUnaryCall(channel, METHOD_GET_CALLER_INFO, options, request)
    }
    
    override def getCalleeInfo(request: protos.dataflow.GetCalleeInfoRequest): protos.dataflow.GetCalleeInfoResponse = {
      _root_.scalapb.grpc.ClientCalls.blockingUnaryCall(channel, METHOD_GET_CALLEE_INFO, options, request)
    }
    
    override def getHeartbeat(request: protos.dataflow.GetHeartbeatRequest): protos.dataflow.GetHeartbeatResponse = {
      _root_.scalapb.grpc.ClientCalls.blockingUnaryCall(channel, METHOD_GET_HEARTBEAT, options, request)
    }
    
    override def receiveComputationUnit(request: protos.dataflow.ReceiveComputationUnitRequest): protos.dataflow.ReceiveComputationUnitResponse = {
      _root_.scalapb.grpc.ClientCalls.blockingUnaryCall(channel, METHOD_RECEIVE_COMPUTATION_UNIT, options, request)
    }
    
    override def setTrigger(request: protos.dataflow.SetTriggerRequest): protos.dataflow.SetTriggerResponse = {
      _root_.scalapb.grpc.ClientCalls.blockingUnaryCall(channel, METHOD_SET_TRIGGER, options, request)
    }
    
    override def build(channel: _root_.io.grpc.Channel, options: _root_.io.grpc.CallOptions): DataflowServerBlockingStub = new DataflowServerBlockingStub(channel, options)
  }
  
  class DataflowServerStub(channel: _root_.io.grpc.Channel, options: _root_.io.grpc.CallOptions = _root_.io.grpc.CallOptions.DEFAULT) extends _root_.io.grpc.stub.AbstractStub[DataflowServerStub](channel, options) with DataflowServer {
    /** Sends a greeting
      */
    override def getCallerInfo(request: protos.dataflow.GetCallerInfoRequest): scala.concurrent.Future[protos.dataflow.GetCallerInfoResponse] = {
      _root_.scalapb.grpc.ClientCalls.asyncUnaryCall(channel, METHOD_GET_CALLER_INFO, options, request)
    }
    
    override def getCalleeInfo(request: protos.dataflow.GetCalleeInfoRequest): scala.concurrent.Future[protos.dataflow.GetCalleeInfoResponse] = {
      _root_.scalapb.grpc.ClientCalls.asyncUnaryCall(channel, METHOD_GET_CALLEE_INFO, options, request)
    }
    
    override def getHeartbeat(request: protos.dataflow.GetHeartbeatRequest): scala.concurrent.Future[protos.dataflow.GetHeartbeatResponse] = {
      _root_.scalapb.grpc.ClientCalls.asyncUnaryCall(channel, METHOD_GET_HEARTBEAT, options, request)
    }
    
    override def receiveComputationUnit(request: protos.dataflow.ReceiveComputationUnitRequest): scala.concurrent.Future[protos.dataflow.ReceiveComputationUnitResponse] = {
      _root_.scalapb.grpc.ClientCalls.asyncUnaryCall(channel, METHOD_RECEIVE_COMPUTATION_UNIT, options, request)
    }
    
    override def setTrigger(request: protos.dataflow.SetTriggerRequest): scala.concurrent.Future[protos.dataflow.SetTriggerResponse] = {
      _root_.scalapb.grpc.ClientCalls.asyncUnaryCall(channel, METHOD_SET_TRIGGER, options, request)
    }
    
    override def build(channel: _root_.io.grpc.Channel, options: _root_.io.grpc.CallOptions): DataflowServerStub = new DataflowServerStub(channel, options)
  }
  
  object DataflowServerStub extends _root_.io.grpc.stub.AbstractStub.StubFactory[DataflowServerStub] {
    override def newStub(channel: _root_.io.grpc.Channel, options: _root_.io.grpc.CallOptions): DataflowServerStub = new DataflowServerStub(channel, options)
    
    implicit val stubFactory: _root_.io.grpc.stub.AbstractStub.StubFactory[DataflowServerStub] = this
  }
  
  def bindService(serviceImpl: DataflowServer, executionContext: scala.concurrent.ExecutionContext): _root_.io.grpc.ServerServiceDefinition = DataflowServer.bindService(serviceImpl, executionContext)
  
  def blockingStub(channel: _root_.io.grpc.Channel): DataflowServerBlockingStub = new DataflowServerBlockingStub(channel)
  
  def stub(channel: _root_.io.grpc.Channel): DataflowServerStub = new DataflowServerStub(channel)
  
  def javaDescriptor: _root_.com.google.protobuf.Descriptors.ServiceDescriptor = protos.dataflow.DataflowProto.javaDescriptor.getServices().get(0)
  
}