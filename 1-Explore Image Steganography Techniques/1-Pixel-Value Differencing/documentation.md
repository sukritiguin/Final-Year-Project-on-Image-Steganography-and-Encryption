# Pixel-Value Differencing

Pixel-value differencing (PVD) is a technique used in image steganography, a field concerned with hiding messages or data within images. In PVD steganography, the goal is to embed secret information into the least significant bits (LSBs) of the pixel values in an image without significantly altering the visual appearance of the image.

## Algorithm

The Pixel-Value Differencing (PVD) algorithm operates by manipulating the differences between adjacent pixel values in an image to embed a secret message. Here's a simplified explanation of how the algorithm works:

1. **Input** : The algorithm takes as input a cover image (the image in which the message will be hidden) and a secret message that needs to be embedded.
2. **Preprocessing (Optional)** : Optionally, the cover image may undergo preprocessing steps such as resizing or converting to grayscale. This step is performed to ensure uniformity and compatibility with the embedding process.
3. **Message Encoding** : The secret message is encoded into a bitstream. This encoding process could involve techniques such as Huffman coding or basic bit packing to efficiently represent the message in binary form.
4. **Difference Calculation** : For each pixel in the cover image, the difference between its value and the value of its neighboring pixel(s) is calculated. Typically, the differences are calculated in a specific direction (e.g., horizontal, vertical, or diagonal) to ensure consistency during embedding and extraction.
5. **LSB Replacement** : The least significant bit (LSB) of each difference value is replaced with a bit from the secret message. This replacement ensures that the changes made to the cover image are minimal and not easily detectable by visual inspection.
6. **Embedding Process** : The modified difference values, now containing bits of the secret message, are used to create the stego image. This process typically involves adjusting the original pixel values using the modified difference values.
7. **Output** : The stego image, which now contains the hidden message, is generated as the output of the algorithm.
8. **Decoding** : To extract the hidden message from the stego image, the reverse process is performed. The differences between adjacent pixel values are calculated, and the LSBs are extracted to reconstruct the embedded message.
9. **Message Decoding** : The extracted bitstream is decoded using the same encoding scheme applied during embedding to retrieve the original secret message.



* ## Difference Calculation

    In Pixel-Value Differencing (PVD) steganography, the first step is to calculate the differences between adjacent pixel values in the cover image. This process is crucial because it forms the basis for embedding the secret message while ensuring minimal 		visual impact on the cover image. Here's how it works:

1. **Neighborhood Selection**: For each pixel in the cover image, a predefined neighborhood is selected. The neighborhood typically consists of neighboring pixels surrounding the target pixel. The size and shape of the neighborhood can vary based on the specific implementation of the PVD algorithm. Common choices include 4-neighbors (left, right, top, bottom) or 8-neighbors (including diagonals).
2. **Difference Calculation**: Once the neighborhood is defined, the next step is to calculate the difference between the pixel value of the target pixel and the pixel values of its neighboring pixels. This calculation can be performed using various methods:

   - **Horizontal Difference**: Calculate the difference between the target pixel and its left or right neighbor.
   - **Vertical Difference**: Calculate the difference between the target pixel and its top or bottom neighbor.
   - **Diagonal Difference**: Calculate the difference between the target pixel and its diagonal neighbors.

   The difference is calculated by subtracting the value of the neighboring pixel from the value of the target pixel. The absolute value of the difference may be taken to ensure that both positive and negative differences are considered.
3. **Bit Depth Consideration**: Depending on the bit depth of the image, the pixel values may be represented using a certain number of bits (e.g., 8 bits for grayscale images or 24 bits for RGB color images). It's important to consider the bit depth when performing the difference calculation to ensure that the resulting difference values fall within an acceptable range.
4. **Normalization (Optional)**: In some implementations, the calculated differences may undergo normalization to limit their range or adjust their distribution. Normalization can help maintain consistency and enhance the effectiveness of the embedding process.
5. **Bit Extraction**: After the differences are calculated, the LSB (least significant bit) of each difference value is typically used to carry a bit of the secret message during the embedding process. The LSB is the rightmost bit in binary representation and is often chosen for steganographic purposes because it tends to have the least impact on the visual appearance of the image.

By calculating the differences between adjacent pixel values and utilizing their LSBs for embedding, the PVD algorithm ensures that the changes made to the cover image are subtle and difficult to detect without knowledge of the embedded message. This approach helps maintain the visual quality of the stego image while effectively hiding the secret information.


It's worth noting that while PVD is a straightforward technique, the effectiveness of the algorithm depends on factors such as the embedding rate (the amount of data that can be hidden without significantly altering the cover image), the choice of encoding scheme, and the robustness of the steganographic method against detection or removal attempts.
