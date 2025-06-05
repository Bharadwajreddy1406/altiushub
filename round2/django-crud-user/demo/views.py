from django.shortcuts import render
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from bson.errors import InvalidId
from first.connection import get_mongo_client


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .authentication import CookieJWTAuthentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken




@api_view
def create_user(request):
    try:
        client = get_mongo_client()
        if not client:
            return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        db = client['userbase']
        collection = db['user']

        userdata = request.data
        print(userdata)
        
        if not userdata or 'firstname' not in userdata:
            return Response({'error': 'firstname field is required'}, status=status.HTTP_400_BAD_REQUEST)
        

        result = collection.insert_one(userdata)
        return Response({
            'message': 'user added successfully', 
            'id': str(result.inserted_id),
            'data': {**userdata, '_id': str(result.inserted_id)}
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
@api_view
def get_all_users(request):
    try:
        client = get_mongo_client()
        if not client:
            return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        db = client['userbase']
        collection = db['user']


        data = []
        for doc in collection.find():
            doc['_id'] = str(doc['_id'])  
            data.append(doc)

        return Response({
            'message': 'users retrieved successfully',
            'data': data,
            'count': len(data)
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PUT', 'PATCH'])
def update_user(request, url_id):
    try:
        client = get_mongo_client()
        if not client:
            return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        db = client['userbase']
        collection = db['user']

        try:
            object_id = ObjectId(url_id)
        except InvalidId:
            return Response({'error': 'Invalid URL ID format'}, status=status.HTTP_400_BAD_REQUEST)

        existing_doc = collection.find_one({'_id': object_id})
        if not existing_doc:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

        update_data = request.data
        if not update_data:
            return Response({'error': 'No data provided for update'}, status=status.HTTP_400_BAD_REQUEST)

        result = collection.update_one(
            {'_id': object_id},
            {'$set': update_data}
        )

        if result.modified_count == 0:
            return Response({'error': 'No changes made'}, status=status.HTTP_304_NOT_MODIFIED)

        updated_doc = collection.find_one({'_id': object_id})
        updated_doc['_id'] = str(updated_doc['_id'])

        return Response({
            'message': 'URL updated successfully',
            'data': updated_doc
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_url(request, user_id):
    try:
        client = get_mongo_client()
        if not client:
            return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        db = client['userbase']
        collection = db['user']
        try:
            object_id = ObjectId(user_id)
        except InvalidId:
            return Response({'error': 'Invalid URL ID format'}, status=status.HTTP_400_BAD_REQUEST)

        existing_doc = collection.find_one({'_id': object_id})
        if not existing_doc:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

        result = collection.delete_one({'_id': object_id})

        if result.deleted_count == 0:
            return Response({'error': 'Failed to delete URL'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'message': 'user id deleted successfully',
            'deleted_id': user_id
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







def home(request):
    context = {
        'name': 'Bharadwaj Reddy',
        'notifications': 3,
        'messages': [
            {'type': 'info', 'text': 'Welcome to the site!'},
            {'type': 'warning', 'text': 'Your profile is incomplete.'},
            {'type': 'success', 'text': 'Your settings have been saved.'}
        ]
    }
    # context = {
    #     'name': 'Bharadwaj Reddy',
    #     'notifications': 3
    # }
    return render(request, 'home.html', context)


def greet(request):
    print(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        messages.success(request, f"Welcome, {name}!")
        if not user_id:
            return render(request, 'form.html', {'error': 'User ID is required'})
        
        return render(request, 'greet.html', {'name': name, 'user_id': user_id})
    
        # return redirect('user', user_id=user_id, name=name)
        
        # return render(request, 'dynamic.html', {'name': name}) # for dynamic URL
    return render(request, 'form.html')
    
    
def dynamic(request,name):
    return render(request, 'dynamic.html', {'name': name})


def user (request, user_id, name):
    return render(request, 'user.html', {'name': name, 'user_id': user_id})








@api_view(['GET'])
@authentication_classes([CookieJWTAuthentication])
@permission_classes([IsAuthenticated])
def test_api(request):
    data = {
        'message': 'This is a test API response',
        'status': 'success'
    }
    return Response(data)
