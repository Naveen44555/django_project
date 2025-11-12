class basicMiddleware:
    def __init__(self,get_response):    #init for to create object
        self.get_response = get_response    #when we run server immediatley run
        
    def __call__(self,request): #when we  request
        print(request,"hello")
        if (request.path=="/student"):
            print(request.method,"method")
            print(request.path,"path")
        response=self.get_response(request) #before going to here view access
        return response
    
# class signupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#         def __call__(self,request):
#             data =json.loads(request.body)
#             username=
