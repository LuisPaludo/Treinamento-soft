import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WeatherService {
  private apiKey = '373d1e6165443ada689d5758cef5341f';

  constructor(private htttp:HttpClient) { }

  getWeatherDatas(cityName: string):Observable<any>
  {
    return this.htttp.get(`https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&mode=json&appid=${this.apiKey}`,
    {})
  }
}
