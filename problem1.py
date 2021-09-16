

def  carParkingRoof(cars, k):
	cars.sort()
	# print(cars)

	covers = []
	for slice in range(0, len(cars)):
		covers.append(cars[slice: slice + k]) if len(cars[slice: slice + k]) == k else None

	differentials = [(cover[-1] - cover[0]) + 1 for cover in covers]
	print(f"[Roof Length Canditates]: {differentials}")
	return min(differentials)


if __name__ == "__main__":
	test_list = [6,2,12,7]
	min_roof_length = carParkingRoof(test_list, k = 3)
	print(f"[Min Roof Length] - {min_roof_length}")