import cv2
import numpy as np
import statistics

############################################################
# Make a 7x7 mean filter. Go!
def meanfilter(image,radius):
  output_image = np.zeros(image.shape, dtype=input_image.dtype)
  for y in range(image.shape[0]):
    if y >= radius and y < image.shape[0] - radius:
      for x in range(image.shape[1]):
        if x >= radius and x < image.shape[1] - radius:
          arr = []
          for x2 in range(radius * 2+1):
            for y2 in range(radius * 2+1):
              pixel = image[y - radius + y2][x - radius + x2]
              arr.append(pixel)
          output_image[y][x] = statistics.mean(arr)
  return output_image

if __name__ == "__main__":
  input_image = cv2.imread("K2/Jeppe/WarmUpExerciseLecture2/lion.jpg", flags=cv2.IMREAD_GRAYSCALE)
  output_image = meanfilter(input_image,5)
  cv2.imwrite("K2/Jeppe/WarmUpExerciseLecture2/output.png", output_image)

  ### Testing the solution ###
  desired_image = cv2.imread("K2/Jeppe/WarmUpExerciseLecture2/desired_output.png", flags=cv2.IMREAD_GRAYSCALE)
  if np.array_equal(output_image, desired_image):
    print("Congratulations! You pass!")
  else:
    print("Wrong! (check for rounding errors)")
