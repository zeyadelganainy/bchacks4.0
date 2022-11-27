package com.example.physicain_android_app;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class mlModelInput extends AppCompatActivity {
    int selectedModel;
    TextView textView;
    ImageView uploadedImage;
    Button gallery, submit;
    String uploadedImageString;
    Bitmap bitmap;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ml_model_input);
        Intent intent = getIntent();
        Bundle bundle = intent.getExtras();
        selectedModel = bundle.getInt("selection");
        uploadedImage = findViewById(R.id.imgGallery);
        gallery = findViewById(R.id.button2);
        submit = findViewById(R.id.button4);

    }
    public void onGalleryClick(View view){
        Intent iGallery = new Intent(Intent.ACTION_PICK);
        iGallery.setData(MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        startActivityForResult(iGallery, 1000);
    }

    public void onSubmit(View view){
        Intent intent = new Intent(mlModelInput.this, httpRequester.class);
        Bundle bundle = new Bundle();
        bundle.putInt("selection",selectedModel);
        bundle.putString("image",uploadedImageString);
        intent.putExtras(bundle);
        startActivity(intent);
    }

protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (resultCode == RESULT_OK)
    {
        Uri imageUri = data.getData();
        uploadedImage.setImageURI(imageUri);
        try{
            bitmap = MediaStore.Images.Media.getBitmap(this.getContentResolver(), imageUri);
            uploadedImageString = BitMapToString(bitmap);
        }
        catch(IOException e){
            System.out.println(e);
        }
    }
}
    public String BitMapToString(Bitmap bitmap){
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.PNG,100, baos);
        byte [] b=baos.toByteArray();
        String temp=Base64.encodeToString(b, Base64.DEFAULT);
        return temp;
    }


}