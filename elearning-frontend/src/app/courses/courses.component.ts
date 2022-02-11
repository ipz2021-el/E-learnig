import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.scss']
})
export class CoursesComponent implements OnInit {

  constructor(private http: HttpClient) { }

  searchword = ''

  search(e: any) {
    this.courses_displayed = this.courses.filter((c:any) => c.title.toLowerCase().includes(this.searchword))
  }

  courses_displayed: any;
  courses:any;
  // courses = [
  //   {
  //     image: 'jupiter-planet',
  //     title: 'Fizyka i astronomia',
  //     tutor: 'Milena Michalska',
  //   },
  //   {
  //     image: 'story-book',
  //     title: 'Czary i magia',
  //     tutor: 'Paweł Gaborek',
  //   },
  //   {
  //     image: 'calculator',
  //     title: 'Analiza matematyczna',
  //     tutor: 'Maciej Lewicki',
  //   },
  //   {
  //     image: 'alcohol-burner',
  //     title: 'Chemia eksperymentalna',
  //     tutor: 'Paweł Gaborek',
  //   },
  //   {
  //     image: 'planetarium',
  //     title: 'Wstęp do obserwacji nieba',
  //     tutor: 'Jan Kowalski',
  //   },
  //   {
  //     image: 'student',
  //     title: 'Seminarium dyplomowe',
  //     tutor: 'Jan Kowalski',
  //   },
  //   {
  //     image: 'biotech',
  //     title: 'Podstawy genetyki',
  //     tutor: 'Jan Kowalski',
  //   },
  //   {
  //     image: 'brain',
  //     title: 'Sztuczna inteligencja',
  //     tutor: 'Jan Kowalski',
  //   }
  // ]

  courses_endpoint() {
    return this.http.get('http://localhost:3000/courses');
  }

  ngOnInit(): void {
    this.courses_endpoint().subscribe((res) => {
      this.courses = res;
      this.courses_displayed = this.courses;
    })
  }

}
