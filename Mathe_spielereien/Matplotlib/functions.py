import matplotlib.pyplot as plt
import numpy as np

def plot_function(functions, x_range=(-10, 10), num_points=1000, title="Plot of f(x)", xlabel="x", ylabel="f(x)"):
    """
    Plots one or more functions over a specified range.
    """
    x = np.linspace(x_range[0], x_range[1], num_points)
    plt.figure(figsize=(8, 6))
    for f in functions:
        y = np.asarray(f(x))
        if y.shape != x.shape:
            print(f"Warning: {f.__name__} returned an array of shape {y.shape} instead of {x.shape}.")
        label = f.__name__ if hasattr(f, '__name__') else "function"
        plt.plot(x, y, label=label)
    plt.yscale("log")  # Use logarithmic scale if needed
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
if __name__ == "__main__":
    # Define functions that compute values directly.
    def function1(x):
        return x

    def function2(x):
        return x**2 * np.log(x)

    def function3(x):
        # Compute the gamma for each element.
        return np.vectorize(lambda t: np.math.gamma(t+1))(x)

    def function4(x):
        return np.log(x)

    def function5(x):
        return 2**x

    def function6(x):
        return x**3

    functions_to_pot = [function1, function2, function3, function4, function5, function6]
    plot_function(functions_to_pot, x_range=(0.1, 10), title="Functionen")