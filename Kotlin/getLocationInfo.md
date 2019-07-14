# KOTLIN

## Get Location Info

### LocationUtils.kt

> FusedLocationProvider를 이용한 기기의 현재 위치가져오기

```kotlin
import android.content.Context
import android.content.Context.LOCATION_SERVICE
import android.content.pm.PackageManager
import android.location.Address
import android.location.Geocoder
import android.location.LocationManager
import android.os.Looper
import android.support.v4.app.ActivityCompat
import android.util.Log
import com.google.android.gms.location.LocationCallback
import com.google.android.gms.location.LocationRequest
import com.google.android.gms.location.LocationResult
import com.google.android.gms.location.LocationServices
import com.studio.jumoneychat.App
import java.io.IOException


class LocationUtils(val context: Context) {
    val TAG = "LocationUtils"
    val fusedLocationClient = LocationServices.getFusedLocationProviderClient(context)
    val locationRequest = LocationRequest.create()
    val locationCallback = object : LocationCallback(){
        override fun onLocationResult(p0: LocationResult?) {
            p0?.let {
                for((i, location) in it.locations.withIndex()) {
                    Log.d(TAG, "#$i ${location.latitude} , ${location.longitude}")
                }
            }
        }
    }
    val geocoder = Geocoder(context)

    fun initLocation() {
        if (ActivityCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            return
        }

        fusedLocationClient.lastLocation
                .addOnSuccessListener { location ->
                    if (location == null) {
                        Log.e(TAG, "location get fail")
                    } else {
                        Log.d(TAG, "${location.latitude} , ${location.longitude}")
                        try{
                            var adress : List<Address> = geocoder.getFromLocation(
                                    location.latitude,
                                    location.longitude,
                                    1
                            )
                            val address = adress.get(0).getAddressLine(0).split(" ")
                            App.myaddress = address[1] + address[2] + address[3]
                            Log.d(TAG, App.myaddress)
                        } catch (e : IOException){
                            Log.d(TAG, "실패")
                        }
                    }
                }
                .addOnFailureListener {
                    Log.e(TAG, "location error is ${it.message}")
                    it.printStackTrace()
                }

    }

    fun requestLocation(){
        if (ActivityCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            return
        }

        locationRequest.run {
            priority = LocationRequest.PRIORITY_HIGH_ACCURACY
            interval = 60 * 1000
        }

        fusedLocationClient.requestLocationUpdates(locationRequest, locationCallback, Looper.myLooper())
    }

    fun stopLocation(){
        fusedLocationClient.removeLocationUpdates(locationCallback)
    }
}
```

#### 1. fun requestLocation()

- `locationRequest.create()` 를 통해서 객체를 생성한다.

- `locationRequest.run` 을 통해서 위치 정보의 정확도와 인터벌을 설정한다

  

#### 2. locationCallback

- locationRequest를 통해 위치정보를 받아올 콜백을 만들어준다.

  

#### 3. fun initLocation()

- `fusedLocationClient.lastLocation` 을통해서 위치데이터를 요청합니다
- 이때 기기의 위치데이터 사용이 체크가 되어있지 않으면 null 데이터를 반환합니다.
- 요청된 데이터는 geocoder를 사용하여 변환시킵니다.



#### 4. geocoder

- 위치정보를 변환해준다. 위도, 경도 정보를 주소정보로 변환
- `getAddressLine(0)` : 대한민국 ~~ 시 ~~ 군 ~~ 까지 주소가 나온다.
- `split(" ")` 을 통해서 위의 정보를 공백기준으로 리스트화 시켜 원하는 데이터만 얻어낸다.



#### 5.stopLocation()

- 위치정보를 받아오는데는 배터리 소모량이 많기 때문에 중지를 위해서 추가
- 보통은 화면이 보이는 시점인 `onResume`에서 작업하고 화면이 사라지는 시점인 `onPause`에서 콜백리스너를 해제시켜야 한다.