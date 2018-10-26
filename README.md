# JPEG2000 Web Service

## API

This is a web service based on OpenJPEG that helps to analyse the content of JPEG2000 images from Sentinel.
It accepts post requests on:
http://IP-ADDRESS/api/jp2

With a payload as follows:
```
{
  "Path": "tiles/33/U/UP/S2A_MSIL1C_20150711T100006_N0204_R122_T33UUP_20160812T055924.SAFE/GRANULE/S2A_OPER_MSI_L1C_TL_EPA__20160811T174848_A000262_T33UUP_N02.04/IMG_DATA/S2A_OPER_MSI_L1C_TL_EPA__20160811T174848_A000262_T33UUP_B8A.jp2",
  "rlevel": -1
}
```

- **Path** is the bucket path of the image that should be analysed.
- **rlevel** can be used to decide on the resolution in which the image will be processed.
`-1` will use the lowest resolution and thus be the fastest.

The service will return sth like:
```
{
  "img_data":
  [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46, 5, 2127, 3938, 4207, 4771, 3422, 2911, 4101, 3691, 4187, 3255, 3964, 3775, 2197, 4149, 2672, 2939, 3405, 4056, 3474, 2907, 3678, 3444, 5261, 3564, 3774, 2794, 4171, 4104, 2664, 4159, 3506, 3832, 5018, 5470, 4956, 4447, 4975, 4929, 4712, 5070, 4707, 4260, 5872, 2889, 3709, 2622, 3805, 2814, 4830, 4277, 3986, 4598, 4397, 4832, 4229, 4751, 4411, 4162, 4123, 4483, 3314, 4645, 4121, 2286, 784, 653 ], [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 59, 293, 3867, 2467, 3322, 3476, 4042, 4157, 3868, 4072, 4336, 4561, 3702, 4533, 0, 3791, 2838, 2570, 3358, 2382, 2402, 1560, 2193, 3958, 3937, 3284, 2884, 3343, 3720, 3777, 5252, 11, 2529, 3729, 3953, 3493, 3519, 3635, 3347, 3240, 3136, 2710, 3012, 1717, 2992, 3904, 4251, 4611, 3350, 2714, 2734, 5088, 2612, 2284, 3326, 3306, 3359, 3236, 3489, 3092, 3686, 1083, 367, 455, 735, 893, 1172, 498, 1284, 3167, 3158, 3473, 3038, 3212, 3792, 4267, 4086, 4006, 3135, 2519, 2373, 2959, 4908, 4074, 3216, 3104, 2400, 2433, 2072, 326, 2764, 3837, 2577, 2793, 4028, 2917, 2528, 1095, 4032, 3362, 2510, 2843, 4322, 4022, 2927, 3558, 2244, 1984, 2691, 4746, 4084, 3973, 4360, 3597, 3121, 3653, 2484, 3867, 3605, 2888, 3029, 3606, 4041, 2562, 3723, 3881, 3762, 3877, 1988, 4003, 3745, 1853, 2402, 2493, 3780, 3774, 4340, 5203, 4168, 2319, 3657, 2672, 3019, 2886, 2617, 2281, 2434, 3458, 3075, 2633, 3082, 3160, 3515, 3334, 4072, 3462, 3046, 3432, 1743, 2882, 3929 ] ],
  "shape": [ 344, 344 ],
  "time_download": 1.545100212097168,
  "time_processing": 0.15723586082458496
  }
```

- **shape** is the height and width of the resolution in which the image has been processed.
- **img_data** contains the color level of each pixel for rows and columns. Note that for an RGB image each pixel would have a value for each color channel, but for Sentinel data the result is just the grey level of each pixel.
- **time_download** the time it took to download the image
- **time_processing** the time it took to process the image

### Example

Using sample.json in `./data`:

```
curl -XPOST -d @sample.json http://IP-ADDRESS/api/jp2 --header "Content-Type: application/json"
```

## Installation

### Requirements
- pip install -r requirements.txt
- OpenJPEG installation
- Gunicorn
- nginx

### Deployment Example

/etc/systemd/system/jp2_service.service
```
[Unit]
Description=Gunicorn instance to serve jp2-service
After=network.target

[Service]
User=jonf
Group=www-data
WorkingDirectory=/home/jonf/src/jp2_service
Environment="PATH=/home/jonf/jp2_service/venv/bin"
ExecStart=/home/jonf/src/jp2_service/venv/bin/gunicorn --workers 4 --bind unix:jp2_service.sock -m 007 jp2_service:app

[Install]
WantedBy=multi-user.target
```

/etc/nginx/sites-enabled/jp2_service
```
server {
    listen 80;
    server_name IP-ADRESS;
        location / {
        include proxy_params;
        proxy_pass http://unix:/home/jonf/src/jp2_service/jp2_service.sock;
    }
}
```



