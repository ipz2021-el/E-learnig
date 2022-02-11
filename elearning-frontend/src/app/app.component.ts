import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {
  title = 'elearning-frontend';
  logged = false;
  logging_step = 'credentials';
  nav = 'dashboard';

  constructor(private http: HttpClient) { }

  // httpOptions = {
  //   headers: new HttpHeaders({
  //     'Content-Type':  'application/json',
  //     Authorization: 'my-auth-token'
  //   })
  // };

  httpOptions = {
    headers: new HttpHeaders({
      'Access-Control-Allow-Origin':  'http://localhost:4200',
    })
  };

  login_endpoint() {
    return this.http.post('http://localhost:8000/users/rest-auth/login/', {
      email: 'milena2@test.pl',
      password: 'mi123lena'
    }, this.httpOptions);
  }

  login() {
    this.login_endpoint()
      .subscribe((res) => {
          console.log(res);
      });
  }
}
