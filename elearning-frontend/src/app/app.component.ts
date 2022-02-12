import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
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
  id = '';
  pass = '';
  err = false;

  constructor(private http: HttpClient, private cookieService: CookieService) { }

  key:any;

  httpOptions:any;

  login_endpoint() {
    return this.http.post('http://127.0.0.1:8000/users/rest-auth/login/', {
      email: 'milena2@test.pl',
      password: 'mi123lena'
    });
  }

  login() {
    if (this.id == 'test' && this.pass == 'test') {
      this.logged = true;
    } else {
      this.err = true;
    }
  }

  courses:any;

  courses_endpoint() {
    return this.http.get('http://localhost:3000/courses');
  }

  ngOnInit(): void {
    this.courses_endpoint().subscribe((res) => {
      this.courses = res
      this.courses = this.courses.filter((c:any) => c.joined);
    })
  }
}
