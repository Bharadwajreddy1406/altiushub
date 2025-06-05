

# @api_view(['GET'])
# def get_collection(request):
#     """Get all URLs from the collection"""
#     try:
#         client = get_mongo_client()
#         if not client:
#             return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         db = client['UrlShortner']
#         collection = db['urls']

#         data = []
#         for doc in collection.find():
#             doc['_id'] = str(doc['_id'])  
#             data.append(doc)

#         return Response({
#             'message': 'URLs retrieved successfully',
#             'data': data,
#             'count': len(data)
#         }, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['GET'])
# def get_url(request, url_id):
#     """Get a specific URL by ID"""
#     try:
#         client = get_mongo_client()
#         if not client:
#             return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         db = client['UrlShortner']
#         collection = db['urls']

#         # Validate ObjectId
#         try:
#             object_id = ObjectId(url_id)
#         except InvalidId:
#             return Response({'error': 'Invalid URL ID format'}, status=status.HTTP_400_BAD_REQUEST)

#         doc = collection.find_one({'_id': object_id})
#         if not doc:
#             return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

#         doc['_id'] = str(doc['_id'])
#         return Response({
#             'message': 'URL retrieved successfully',
#             'data': doc
#         }, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['POST'])
# def add_url(request):
#     """Create a new URL entry"""
#     try:
#         client = get_mongo_client()
#         if not client:
#             return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         db = client['UrlShortner']
#         collection = db['urls']

#         url_data = request.data
#         print(url_data)
        
#         # Validate required fields
#         if not url_data or 'url' not in url_data:
#             return Response({'error': 'URL field is required'}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Add timestamp
#         from datetime import datetime
#         url_data['created_at'] = datetime.utcnow()
#         url_data['updated_at'] = datetime.utcnow()

#         result = collection.insert_one(url_data)
#         return Response({
#             'message': 'URL added successfully', 
#             'id': str(result.inserted_id),
#             'data': {**url_data, '_id': str(result.inserted_id)}
#         }, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['PUT', 'PATCH'])
# def update_url(request, url_id):
#     """Update an existing URL entry"""
#     try:
#         client = get_mongo_client()
#         if not client:
#             return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         db = client['UrlShortner']
#         collection = db['urls']

#         # Validate ObjectId
#         try:
#             object_id = ObjectId(url_id)
#         except InvalidId:
#             return Response({'error': 'Invalid URL ID format'}, status=status.HTTP_400_BAD_REQUEST)

#         # Check if document exists
#         existing_doc = collection.find_one({'_id': object_id})
#         if not existing_doc:
#             return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

#         update_data = request.data
#         if not update_data:
#             return Response({'error': 'No data provided for update'}, status=status.HTTP_400_BAD_REQUEST)

#         # Add updated timestamp
#         from datetime import datetime
#         update_data['updated_at'] = datetime.utcnow()

#         # Update the document
#         result = collection.update_one(
#             {'_id': object_id},
#             {'$set': update_data}
#         )

#         if result.modified_count == 0:
#             return Response({'error': 'No changes made'}, status=status.HTTP_304_NOT_MODIFIED)

#         # Get updated document
#         updated_doc = collection.find_one({'_id': object_id})
#         updated_doc['_id'] = str(updated_doc['_id'])

#         return Response({
#             'message': 'URL updated successfully',
#             'data': updated_doc
#         }, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['DELETE'])
# def delete_url(request, url_id):
#     """Delete a URL entry"""
#     try:
#         client = get_mongo_client()
#         if not client:
#             return Response({'error': 'Database connection failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#         db = client['UrlShortner']
#         collection = db['urls']

#         # Validate ObjectId
#         try:
#             object_id = ObjectId(url_id)
#         except InvalidId:
#             return Response({'error': 'Invalid URL ID format'}, status=status.HTTP_400_BAD_REQUEST)

#         # Check if document exists
#         existing_doc = collection.find_one({'_id': object_id})
#         if not existing_doc:
#             return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Delete the document
#         result = collection.delete_one({'_id': object_id})

#         if result.deleted_count == 0:
#             return Response({'error': 'Failed to delete URL'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         return Response({
#             'message': 'URL deleted successfully',
#             'deleted_id': url_id
#         }, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['POST'])
# def login_with_cookies(request):
#     """
#     Custom login view that sets JWT tokens in cookies
#     """
#     username = request.data.get('username')
#     password = request.data.get('password')
    
#     if not username or not password:
#         return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    
#     user = authenticate(username=username, password=password)
#     if user:
#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)
#         refresh_token = str(refresh)
        
#         response = Response({
#             'message': 'Login successful',
#             'user': {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email
#             }
#         }, status=status.HTTP_200_OK)
        
#         # Set tokens in cookies
#         response.set_cookie(
#             'access_token', 
#             access_token, 
#             max_age=3600,  # 1 hour
#             httponly=True,
#             secure=False,  # Set to True in production with HTTPS
#             samesite='Lax'
#         )
#         response.set_cookie(
#             'refresh_token', 
#             refresh_token, 
#             max_age=86400,  # 1 day
#             httponly=True,
#             secure=False,  # Set to True in production with HTTPS
#             samesite='Lax'
#         )
        
#         return response
#     else:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def logout_cookies(request):
#     """
#     Logout view that clears JWT cookies
#     """
#     response = Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
#     response.delete_cookie('access_token')
#     response.delete_cookie('refresh_token')
#     return response



