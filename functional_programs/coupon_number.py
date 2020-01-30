from utility import Utility

coupon_object = Utility()

size = int(input("Enter size of the list"))

distinct_list = coupon_object.list_creation(size)

print(f"Count of random numbers generated: {coupon_object.coupon_number(distinct_list)}")

