from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AttendanceSerializer,UsersSerializer,MarkSerializer,RoleSerializer,StudentSerializer,TeacherSerializer,HodSerializer
from Core.models import User,Role,Attendance,Mark,Student,Hod,Teacher
from rest_framework import status



class UserAPI(APIView):
    def get(self,request):
        try:
            user_id = request.query_params.get('students_id')

            if user_id:
             obj = User.objects.get(id=user_id)    
             serializer = UsersSerializer(obj, many=True)
             return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
                    return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
         

    def post(self,request):
        try:
            data=request.data
            serializer=UsersSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("successfully created",status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


    def put(self,request):
        try:
            
            serializer1=Users.objects.get(id=request.data['id'])

            serializer=UsersSerializer(serializer1,data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data,status=status.HTTP_202_ACCEPTED)  
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


class RoleAPI(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=RoleSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("successfully created",status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)       

class AttendanceAPI(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=AttendanceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("successfully created",status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

    def get(self,request):
            user_id = request.query_params.get('user_id')
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            try:
                obj = User.objects.get(id=user_id)
                if obj:
                    attendance_qs = Attendance.objects.filter(user_id=user_id)

                    if start_date and end_date:
                        attendance_qs = attendance_qs.filter(date__range=[start_date, end_date])

                    data = {
                        "info": UsersSerializer(obj).data, 
                        "attendance_details": AttendanceSerializer(attendance_qs, many=True).data
                    }
                    return Response(data,status=status.HTTP_200_OK)   
            except Exception as e:
             raise Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MarkAPI(APIView):
    
    def post(Self,request):
        try:
            data=request.data
            serializer=MarkSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("successfully created",status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)                      


    
class StudentAPI(APIView) :
    def post(self,request):
        try:
            data=request.data
            serializer=StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("successfully created",status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
    

    def get(self,request):
        try:
            student_id = request.query_params.get('student_id')
            instance = Student.objects.get(id=student_id)
            marks = Mark.objects.get(student_id=instance.id)
            data={
                "student_info":StudentSerializer(instance).data,
                "marks_info":MarkSerializer(marks).data 
            }
            return Response(data,status=status.HTTP_200_OK)
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:   
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       

class TeacherAPI(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=TeacherSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("successfully created",status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

class HodAPI(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=HodSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("successfully created",status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

    def get(self,request):

        hod_id=request.query_params.get('hod_id')
        try:

            obj=Hod.objects.get(id=hod_id)
            serializer=HodSerializer(obj)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message":str(e)})    






                                    