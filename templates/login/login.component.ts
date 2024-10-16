import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;

  constructor(private fb: FormBuilder) {
    // Initialiser le formulaire de connexion
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  ngOnInit(): void {
  }

  // Méthode soumise lors de la validation du formulaire
  onSubmit(): void {
    if (this.loginForm.valid) {
      console.log("Formulaire de connexion valide : ", this.loginForm.value);
      // Appeler le service d'authentification ici
    } else {
      console.log("Formulaire invalide !");
    }
  }

  // Getter pour un accès facile aux contrôles de formulaire dans le template
  get f() { return this.loginForm.controls; }

}
