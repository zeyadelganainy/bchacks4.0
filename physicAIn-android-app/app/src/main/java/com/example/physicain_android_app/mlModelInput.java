package com.example.physicain_android_app;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class mlModelInput extends AppCompatActivity {
    int selectedModel;
    ImageView uploadedImage;
    Button gallery;
    private final int GALLERY_REQ_CODE = 1000;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ml_model_input);
        Intent intent = getIntent();
        Bundle bundle = intent.getExtras();
        selectedModel = bundle.getInt("selection");
        uploadedImage = findViewById(R.id.imgGallery);
        gallery = findViewById(R.id.button2);

    }
    public void onClick(View v){
        Intent iGallery = new Intent(Intent.ACTION_PICK);
        iGallery.setData(MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        startActivityForResult(iGallery, GALLERY_REQ_CODE);
    }

    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data){
        super.onActivityResult(requestCode, resultCode, data);

        if(resultCode == RESULT_OK){
            if(requestCode== GALLERY_REQ_CODE){
                uploadedImage.setImageURI(data.getData());
            }
        }
    }
}