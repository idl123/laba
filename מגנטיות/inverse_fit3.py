from eddington import fitting_function

@fitting_function(
	n=3,
	save = True,
	syntax ="(a[0])/((x + a[1])**3) + a[2]")

def inverse_fit3(a, x):
    return (a[0])/((x + a[1])**3) + a[2]