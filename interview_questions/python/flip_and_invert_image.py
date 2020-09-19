# https://leetcode.com/problems/flipping-an-image/solution/
def invert_image(image):
            for i in range(len(image)):
                for j in range(len(image[i])):
                    image[i][j] = 1 if image[i][j] == 0 else 0
            return image

        def reverse_image(image):
            for i in range(len(image)):
                image[i] = list(reversed(image[i]))
            return image


        def flip_image(image):
            return reverse_image(invert_image(image))
        return flip_image(A)

