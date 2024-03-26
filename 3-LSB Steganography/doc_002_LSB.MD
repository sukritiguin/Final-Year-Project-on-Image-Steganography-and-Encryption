# LSBSteganography Algorithm Documentation:


Steganography is the practice of concealing secret information within a carrier medium, such as text, image, audio, or video, in a way that the existence of the hidden information is not apparent to unintended recipients. Unlike cryptography, which focuses on making the content of a message unreadable to unauthorized users, steganography aims to hide the fact that a secret message exists.

LSB (Least Significant Bit) steganography is a common technique used to hide information within digital images. In LSB steganography, the least significant bits of the pixel values in an image are altered to encode the hidden data. Since the least significant bits have the least impact on the visual appearance of the image, modifying them does not significantly alter the image's perceptual quality. LSB steganography is particularly effective because it allows for the hiding of data within an image while minimizing the noticeable changes to the image's appearance.

The process of LSB steganography typically involves the following steps:

1. **Selecting a Cover Medium**: A digital image is chosen as the cover medium to conceal the secret message.
2. **Converting Data**: The secret message, which can be text, another image, or any digital data, is converted into a binary format.
3. **Embedding Data**: The binary data is then embedded into the least significant bits of the pixel values of the cover image. Each pixel in the image typically consists of three color channels (e.g., red, green, blue in an RGB image), and the least significant bit of each channel is modified to encode a bit of the secret message.
4. **Retrieving Data**: To extract the hidden message from the stego image, the LSBs of the pixel values are examined and decoded to reconstruct the original binary data. This data is then converted back into its original format to reveal the hidden message.

LSB steganography is widely used due to its simplicity and effectiveness. However, it may not be suitable for transmitting highly sensitive information as it can be vulnerable to detection by adversaries with sophisticated analysis techniques. Additionally, LSB steganography is primarily applicable to digital images and may not be suitable for other types of media.


## Working Principle


The LSB (Least Significant Bit) steganography technique operates on the principle of modifying the least significant bits of the pixel values in an image to embed data without significantly altering the visual appearance of the image. Here's the working principle of the LSBSteganography algorithm:

1. **Initialization**:

   - The LSBSteganography class is initialized with the path of the cover image.
   - The cover image is opened using the Python Imaging Library (PIL), and its dimensions are retrieved.
2. **Embedding Text**:

   - The `hide_text` method is called with the text to hide as input.
   - Each character in the text is converted to its ASCII value.
   - The binary representation of each ASCII value is obtained.
   - The LSBs of the RGB values of pixels in the last row of the image are replaced with the bits of the binary representation of ASCII values.
   - A backspace ASCII character (8) is used to mark the end of the hidden text.
3. **Extracting Text**:

   - The `extract_text` method is called to extract the hidden text from the stego image.
   - The LSBs of the RGB values of pixels in the last row of the stego image are examined.
   - The LSBs are concatenated to form binary data.
   - The binary data is converted back to ASCII characters.
   - Extraction stops when the backspace ASCII character (8) is encountered, indicating the end of the hidden text.
4. **Saving the Stego Image**:

   - The `save_stego_image` method is called to save the stego image with the embedded text.
5. **Example Usage**:

   - An instance of the LSBSteganography class is created with the cover image path.
   - The text to hide is specified.
   - The text is embedded in the image using LSB steganography.
   - The stego image is saved.
   - The hidden text is extracted from the stego image.

By modifying the LSBs of the pixel values, LSB steganography allows for the embedding of data within an image while minimally impacting its visual appearance. This technique is often used for hiding messages or information within digital images for covert communication or data concealment purposes.
