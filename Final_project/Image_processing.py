import cv2
import numpy as np
import rasterio

### Open 2015 - 2024 Salmon Creek imagery
### Load images as datasets and then find the Red and NIR layers in the .tif files.
with rasterio.open("Final_project/FLX_Orthoimagery/m_4207628_se_18_h_20150724.tif") as dataset_2015:
    R1 = dataset_2015.read(1).astype(np.float32)
    NIR1 = dataset_2015.read(4).astype(np.float32)
    SC_2015 = dataset_2015.read()

with rasterio.open("Final_project/FLX_Orthoimagery/m_4207628_se_18_1_20171017.tif") as dataset_2017:
    R2 = dataset_2017.read(1).astype(np.float32)
    NIR2 = dataset_2017.read(4).astype(np.float32)
    SC_2017 = dataset_2017.read()

with rasterio.open("Final_project/FLX_Orthoimagery/m_4207628_se_18_060_20190918.tif") as dataset_2019:
    R3 = dataset_2019.read(1).astype(np.float32)
    NIR3 = dataset_2019.read(4).astype(np.float32)
    SC_2019 = dataset_2019.read()

with rasterio.open("Final_project/FLX_Orthoimagery/m_4207628_se_18_060_20210824.tif") as dataset_2021:
    R4 = dataset_2021.read(1).astype(np.float32)
    NIR4 = dataset_2021.read(4).astype(np.float32)
    SC_2021 = dataset_2021.read()

with rasterio.open("Final_project/FLX_Orthoimagery/m_4207628_se_18_060_20241018.tif") as dataset_2024:
    R5 = dataset_2024.read(1).astype(np.float32)
    NIR5 = dataset_2024.read(4).astype(np.float32)
    SC_2024 = dataset_2024.read()

### Set the NoData values to 0 for each dataset
R1[R1 == dataset_2015.nodata] = 0
R2[R2 == dataset_2017.nodata] = 0
R3[R3 == dataset_2019.nodata] = 0
R4[R4 == dataset_2021.nodata] = 0
R5[R5 == dataset_2024.nodata] = 0

### Set bincolor to 0 for each dataset
NIR1[NIR1 == dataset_2015.nodata] = 0
NIR2[NIR2 == dataset_2017.nodata] = 0
NIR3[NIR3 == dataset_2019.nodata] = 0
NIR4[NIR4 == dataset_2021.nodata] = 0
NIR5[NIR5 == dataset_2024.nodata] = 0

### Convert datasets to images for display
img_2015 = cv2.merge([SC_2015[2], SC_2015[1], SC_2015[0]])
img_2017 = cv2.merge([SC_2017[2], SC_2017[1], SC_2017[0]])
img_2019 = cv2.merge([SC_2019[2], SC_2019[1], SC_2019[0]])
img_2021 = cv2.merge([SC_2021[2], SC_2021[1], SC_2021[0]])
img_2024 = cv2.merge([SC_2024[2], SC_2024[1], SC_2024[0]])

### Calculating NDVI for each year using the formula: NDVI = (NIR - Red) / (NIR + Red)

NDVI_2015 = (NIR1 - R1) / (NIR1 + R1)
NDVI_2017 = (NIR2 - R2) / (NIR2 + R2)
NDVI_2019 = (NIR3 - R3) / (NIR3 + R3)
NDVI_2021 = (NIR4 - R4) / (NIR4 + R4)
NDVI_2024 = (NIR5 - R5) / (NIR5 + R5)

### Vegetation extent and thresholding
NDVI_threshold = 0.3
veg_2015 = NDVI_2015 > NDVI_threshold
veg_2017 = NDVI_2017 > NDVI_threshold
veg_2019 = NDVI_2019 > NDVI_threshold
veg_2021 = NDVI_2021 > NDVI_threshold
veg_2024 = NDVI_2024 > NDVI_threshold

### Binary masks for vegetation extent
veg_mask_2015 = veg_2015.astype(np.uint8) * 255
veg_mask_2017 = veg_2017.astype(np.uint8) * 255
veg_mask_2019 = veg_2019.astype(np.uint8) * 255
veg_mask_2021 = veg_2021.astype(np.uint8) * 255
veg_mask_2024 = veg_2024.astype(np.uint8) * 255

### NDVI image mask
NDVI_mask_2015 = cv2.applyColorMap(((NDVI_2015 + 1) * 127.5).astype(np.uint8), cv2.COLORMAP_WINTER)
NDVI_mask_2017 = cv2.applyColorMap(((NDVI_2017 + 1) * 127.5).astype(np.uint8), cv2.COLORMAP_WINTER)
NDVI_mask_2019 = cv2.applyColorMap(((NDVI_2019 + 1) * 127.5).astype(np.uint8), cv2.COLORMAP_WINTER)
NDVI_mask_2021 = cv2.applyColorMap(((NDVI_2021 + 1) * 127.5).astype(np.uint8), cv2.COLORMAP_WINTER)
NDVI_mask_2024 = cv2.applyColorMap(((NDVI_2024 + 1) * 127.5).astype(np.uint8), cv2.COLORMAP_WINTER)

### Resize images for display
NDVI_mask_2015 = cv2.resize(NDVI_mask_2015, (800, 600))
NDVI_mask_2017 = cv2.resize(NDVI_mask_2017, (800, 600))
NDVI_mask_2019 = cv2.resize(NDVI_mask_2019, (800, 600))
NDVI_mask_2021 = cv2.resize(NDVI_mask_2021, (800, 600))
NDVI_mask_2024 = cv2.resize(NDVI_mask_2024, (800, 600))

cv2.waitKey(0)
cv2.destroyAllWindows()

### Export NDVI and vegetation extent masks as .tif files
# with rasterio.open("Final_project/NDVI_2015.tif", "w",
#                    driver="GTiff", width=NDVI_2015.shape[1], 
#                    height=NDVI_2015.shape[0], count=1, dtype=NDVI_2015.dtype) as dst:
#     dst.write(NDVI_2015, 1)

# with rasterio.open("Final_project/NDVI_2017.tif", "w",
#                    driver="GTiff", width=NDVI_2017.shape[1], 
#                    height=NDVI_2017.shape[0], count=1, dtype=NDVI_2017.dtype) as dst:
#     dst.write(NDVI_2017, 1)

# with rasterio.open("Final_project/NDVI_2019.tif", "w",
#                    driver="GTiff", width=NDVI_2019.shape[1], 
#                    height=NDVI_2019.shape[0], count=1, dtype=NDVI_2019.dtype) as dst:
#     dst.write(NDVI_2019, 1)

# with rasterio.open("Final_project/NDVI_2021.tif", "w",
#                    driver="GTiff", width=NDVI_2021.shape[1], 
#                    height=NDVI_2021.shape[0], count=1, dtype=NDVI_2021.dtype) as dst:
#     dst.write(NDVI_2021, 1)

# with rasterio.open("Final_project/NDVI_2024.tif", "w",
#                    driver="GTiff", width=NDVI_2024.shape[1], 
#                    height=NDVI_2024.shape[0], count=1, dtype=NDVI_2024.dtype) as dst:
#     dst.write(NDVI_2024, 1)

### Determine the change in vegetation extent between each year
veg_change_1 = veg_2017.astype(np.int8) - veg_2015.astype(np.int8)
veg_change_2 = veg_2019.astype(np.int8) - veg_2017.astype(np.int8)
veg_change_3 = veg_2021.astype(np.int8) - veg_2019.astype(np.int8)
veg_change_4 = veg_2024.astype(np.int8) - veg_2021.astype(np.int8)

print("Vegetation change from 2015 to 2017:", np.sum(veg_change_1))
print("Vegetation change from 2017 to 2019:", np.sum(veg_change_2))
print("Vegetation change from 2019 to 2021:", np.sum(veg_change_3))
print("Vegetation change from 2021 to 2024:", np.sum(veg_change_4))