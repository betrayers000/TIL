# KOTLIN

## 기기의 갤러리에서 이미지 가져오기

### 1. 이미지 뷰어 모양 설정

- 둥근 모양으로 설정

  ```kotlin
  pro_img.background = ShapeDrawable(OvalShape())
  pro_img.clipToOutline = true
  ```

### 2. 새로운 Activity를 띄우고 해당 Activity에서 결과값 가져오기

```kotlin
fun selectGallery(){
    val intent = Intent(Intent.ACTION_PICK)
    intent.setData(android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI)
    intent.setType("image/*")
    startActivityForResult(intent, GALLERY_CODE)
}

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    if(resultCode == Activity.RESULT_OK){
        when(requestCode){
            GALLERY_CODE -> {
                bitmap = ImageUtils(this).getPicture(data!!.data)
                imgPath = data.data
            }
            else -> {

            }
        }
    }
}
```

- `startActivityForResult` 를 사용해서 `onActivityResult`의 결과를 이 액티비티로 가져온다.
- 후속 액티비티에서 작업한 결과물을 호출한 액티비티에서 사용하고 싶은 경우에 사용한다.
- `GALLRY_CODE` : '요청코드'를 통해서 결과값을 반환할때 결과를 식별하여 처리가능합니다.
- `when(requestCode)` 코드를 통해서 결과를 식별

### 3. 로컬 저장소에서 이미지 가져오기

```kotlin
class ImageUtils(val context : Context) {
    /**
     * 이미지를 이미지 뷰어로 불러오기
     */
    fun getPicture(imgUri : Uri) : Bitmap {
        val imagePath = getRealPath(imgUri)
        var exif : ExifInterface? = null
        try{
            exif = ExifInterface(imagePath)
        } catch (e : Exception){
            e.printStackTrace()
        }
        val exifOrientation = exif!!.getAttributeInt(ExifInterface.TAG_ORIENTATION, ExifInterface.ORIENTATION_NORMAL)
        val exifDegree = exifOrientationToDegree(exifOrientation)
        Log.d("test_success", imagePath)
        val bitmap = BitmapFactory.decodeFile(imagePath)
        return rorate(bitmap, exifDegree.toFloat())
    }

    //이미지 회전값 구하기
    fun exifOrientationToDegree(exifOrientation : Int) : Int{
        if(exifOrientation == ExifInterface.ORIENTATION_ROTATE_90){
            return 90
        } else if(exifOrientation == ExifInterface.ORIENTATION_ROTATE_180){
            return 180
        } else if(exifOrientation == ExifInterface.ORIENTATION_ROTATE_270){
            return 270
        }
        return 0
    }
    //정방향으로 회전시키기
    fun rorate(src : Bitmap, degree : Float) : Bitmap {
        val matrix = Matrix()
        matrix.postRotate(degree)
        return Bitmap.createBitmap(src, 0, 0, src.width, src.height, matrix, true)
    }
    //이미지 절대 경로 구하기
    fun getRealPath(contentUri : Uri) : String{
        var column_index = 0
        val proj  = arrayOf(MediaStore.Images.Media.DATA)
        var cursor = context.contentResolver.query(contentUri, proj, null, null, null)
        if(cursor.moveToFirst()){
            column_index = cursor.getColumnIndexOrThrow(MediaStore.Images.Media.DATA)
        }
        return cursor.getString(column_index)
    }
}
```

### 4. 이미지 크기 조정

```kotlin
//이미지 리사이즈
fun resize(uri : Uri, resize : Int ) : Bitmap {
    var resizeBitmap: Bitmap? = null
    val options = BitmapFactory.Options()
    try {
        BitmapFactory.decodeStream(context.contentResolver.openInputStream(uri), null, options)

        var width = options.outWidth
        var height = options.outHeight
        var samplesize = 2

        while (true) {
            if (width / 2 < resize || height / 2 < resize)
            break
            width /= 2
            height /= 2
            samplesize += 2
        }
        options.inSampleSize = samplesize
        val bitmap: Bitmap = BitmapFactory.decodeStream(context.contentResolver.openInputStream(uri), null, options)
        resizeBitmap = bitmap
    } catch (e: FileNotFoundException) {
        e.printStackTrace()
    }
    return resizeBitmap!!
}
```

- 이미지를 서버로 전송하기 위해 용량 조정을 위해서 resize 한다.
- `var samplesize` 를 통해서 이미지의 크기를 조정

