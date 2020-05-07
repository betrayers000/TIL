# Android realtime update view

> Android에서 textview를 실시간으로 업데이트하기 위해서는 thread를 이용해야 한다.
>
> Thread 클래스 안에서 `runOnUiThread` 를 이용하여 view를 update해야 실시간으로 적용이 된다.

### MainActivity.kt

```kotlin
inner class ThreadClass() : Thread(){
   
        override fun run() {
          //Thread로 실행할 작업
            while(loopChk){
              // Thread로 반복해서 할 작업 -> 이 작업을 통해서 view에 변화를 줄 작업을 한다. 
                    runOnUiThread {
                      // view update 작업
                    }
                }
            }
        }
    }
```



