import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  constructor(private http: HttpClient) { }

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
