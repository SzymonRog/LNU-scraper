function checkWeather(temperature){
    if(temperature >= 30){
        return "Upał!"
    }else if(temperature >= 20){
        return "Ładna pogoda"
    }else if(temperature >= 10){
        return "Chłodno"
    }else{
        return "Zimno"
    }
}