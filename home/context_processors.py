from datetime import datetime

def site_info(request):
    return{
        "current_year": datetime.now().year,
        "restaurant_name": "My Restaurant",
        "opening_hours_str": "Mon-Fri: 11am-9pm . Sat-Sun: 10am-10pm",
    }