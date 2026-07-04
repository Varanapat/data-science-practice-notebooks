# Image Preprocessing for OCR

This folder contains a Jupyter Notebook that demonstrates image preprocessing techniques for **Optical Character Recognition (OCR)**. The main objective is to show how different preprocessing methods can improve the accuracy of **Tesseract OCR (`pytesseract`)** before extracting text from images.

---

## Project Structure

| File                      | Description                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| `OCR.ipynb`               | Main notebook demonstrating image preprocessing techniques and OCR.       |
| `text_image1.png`         | Sample image for OCR experiments.                                         |
| `text_image2.jpg`         | Primary sample image used throughout the notebook.                        |
| `text_image2_rotated.jpg` | Rotated sample image for testing image deskewing and rotation correction. |

---

## What You'll Learn

The notebook covers several common image preprocessing techniques used before OCR, including:

* Loading and displaying images using **Pillow**, **OpenCV**, and **Matplotlib**
* Converting images to grayscale
* Binary thresholding (binarization)
* Image inversion
* Noise reduction using:

  * Dilation
  * Erosion
  * Morphological operations
  * Median blur
* Adjusting text thickness
* Correcting image skew using:

  * Contour-based deskewing
  * Hough Line Transform
* Removing unnecessary image borders
* Adding image padding to improve OCR performance
* Extracting text using **pytesseract**

---

## Technologies Used

* Python
* OpenCV (`opencv-python`)
* Pillow
* NumPy
* Matplotlib
* pytesseract
* Tesseract OCR

---

## Running on Google Colab

### 1. Open the notebook

Open `OCR.ipynb` in Google Colab.

### 2. Install the required Python packages

```python
!pip install pillow
!pip install opencv-python
!pip install pytesseract
```

### 3. Install Tesseract OCR

If your environment does not already include Tesseract, install it using:

```python
!sudo apt install tesseract-ocr
```

### 4. Prepare the sample images

Upload the sample images or place them in the directory expected by the notebook, for example:

```text
data/text_image2.jpg
data/text_image2_rotated.jpg
```

### 5. Run the notebook

Execute the notebook step by step, starting from image loading, preprocessing, and finally OCR text extraction.

---

## Notebook Workflow

### 1. Load Image

Load images using **Pillow** and **OpenCV** to inspect image properties, visualize the image, and perform basic image rotation.

### 2. Image Preprocessing

Apply preprocessing techniques before OCR, including:

* Image inversion
* Grayscale conversion
* Thresholding (binarization)
* Noise removal
* Dilation and erosion
* Deskewing and rotation correction
* Border removal
* Border padding

### 3. OCR

Extract text from the preprocessed image using `pytesseract`.

```python
ocr_result = pytesseract.image_to_string(denoised_img)
print(ocr_result)
```

---

## Notes

OCR accuracy depends heavily on image quality, including lighting conditions, image resolution, text size, skew angle, and noise. Applying appropriate preprocessing techniques can significantly improve text recognition performance before passing the image to Tesseract OCR.
