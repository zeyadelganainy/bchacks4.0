package com.example.physicain_android_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class chatbot extends AppCompatActivity {
    Button eye, tooth, skin;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chatbot);

        eye = findViewById(R.id.button7);
        tooth = findViewById(R.id.button6);
        skin = findViewById(R.id.button3);
    }

    public void eyeSelector(View view){
        sendInput(1);
    }


    public void toothSelector(View view){
        sendInput(2);
    }


    public void skinSelector(View view){
        sendInput(3);
    }

    void sendInput(int selection){

        Intent intent = new Intent(chatbot.this, mlModelInput.class);
        Bundle bundle = new Bundle();
        bundle.putInt("selection",selection);
        intent.putExtras(bundle);
        startActivity(intent);
    }
}