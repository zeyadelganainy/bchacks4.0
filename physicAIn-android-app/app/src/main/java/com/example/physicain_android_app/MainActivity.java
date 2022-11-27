package com.example.physicain_android_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    Button begin;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        begin = findViewById(R.id.button);
    }

    public void beginHere(View view){
        Intent intent = new Intent(this, chatbot.class);
        startActivity(intent);
    }
}