import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

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

  constructor(private http: HttpClient, private cookieService: CookieService) { }

  key:any;

  httpOptions:any;

  login_endpoint() {
    return this.http.post('http://127.0.0.1:8000/users/rest-auth/login/', {
      email: 'milena2@test.pl',
      password: 'mi123lena'
    });
  }

  courses_endpoint() {
    return this.http.post('http://127.0.0.1:8000/courses/create', {
      owner: {email: 'milena2@test.pl'},
      subject: {title: "chemia", slug: "chemia"},
      title:"kurs chemii",
      modules: [
        {
          title: "chemia 1",
          description: "modul chemia 1",
        },
        {
          title: "chemia 2",
          description: "modul chemia 2",
          contents: {content_type: "text/video/image/file", object_id: 1}
        }
      ]
    }, this.httpOptions);
  }

  add_course() {
    this.courses_endpoint().subscribe((res) => {
      console.log(res);
    });
  }

  login() {
    this.login_endpoint()
      .subscribe((res) => {
          this.key = res;
          this.key = this.key.key
          console.log(this.key);

          this.cookieService.set('XSRF-TOKEN', this.key);

          this.httpOptions = {
            headers: new HttpHeaders({
              'Content-Type':  'application/json',
              'Authorization': 'Token ' + this.key,
            })
          };
      });
  }
}
