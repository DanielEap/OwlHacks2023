from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

def clarifai_api_call(raw_text):
    api_key = '19d8e93560884750b37a6ce7efa6f157'
    user_id = 'openai'
    app_id = 'chat-completion'
    model_id = 'GPT-4'
    model_version_id = 'ad16eda6ac054796bf9f348ab6733c72'
    
    # Initialize the Clarifai gRPC channel
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + api_key),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=user_id, app_id=app_id)

    # Make the API call
    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,
            model_id=model_id,
            version_id=model_version_id,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw=raw_text
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )

    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]

    return output.data.text.raw

