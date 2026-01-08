from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant, Food


def restaurant_list(request):
    """
    API endpoint to get the list of all restaurants.
    """
    restaurants = Restaurant.objects.all()
    data = [{"resID": restaurant.resID, "resName": restaurant.resName} for restaurant in restaurants]
    return JsonResponse(data, safe=False)


def restaurant_detail(request, restaurant_id):
    """
    API endpoint to get the details of a specific restaurant.
    """
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        data = {
            "resID": restaurant.resID,
            "resName": restaurant.resName,
            "location": restaurant.location,
            "cateID": restaurant.cateID.ID,  # Assuming you want the ID of the related RestaurantType
            "branch": restaurant.branch,
            "phone": restaurant.phone,
        }
        return JsonResponse(data)
    except Restaurant.DoesNotExist:
        return JsonResponse({"error": "Restaurant not found"}, status=404)


def food_list_by_restaurant(request, restaurant_id):
    """
    API endpoint to get a list of food items for a specific restaurant.
    """
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        food_items = Food.objects.filter(resID=restaurant)
        data = [
            {
                "foodID": food.foodID,
                "foodName": food.foodName,
                "price": food.price,
                "description": food.description,
                "image": food.image,
            }
            for food in food_items
        ]
        return JsonResponse(data, safe=False)
    except Restaurant.DoesNotExist:
        return JsonResponse({"error": "Restaurant not found"}, status=404)


def home(request):
    """
    Basic view for the home page.
    """
    return render(request, 'home.html')  #  Make sure you have a template named home.html