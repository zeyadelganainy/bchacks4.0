package com.example.physicain_android_app;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import android.app.DownloadManager;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.textclassifier.TextLinks;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.HttpResponse;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.jetbrains.annotations.NotNull;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URI;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.ResponseBody;
import okhttp3.internal.http.StatusLine;

public class httpRequester extends AppCompatActivity {

    TextView textView;
    String model;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_http_requester);
        OkHttpClient client = new OkHttpClient();
        Intent intent = getIntent();
        Bundle bundle = intent.getExtras();
        int s = bundle.getInt("selection");
        String image = bundle.getString("image");
        switch(s){
            case 1: model = "eye-disease"; break;
            case 2: model = "cavity"; break;
            case 3: model = "skin-cancer"; break;
            default:
                model = null;
        }
        textView = findViewById(R.id.textView5);
        textView.setText("No");
        HttpUrl httpUrl = new HttpUrl.Builder()
                .scheme("http")
                .host("34.125.63.206")
                .port(5000)
                .addPathSegment("admin")
                .addQueryParameter("model", model)
                .addQueryParameter("image", image)
                .build();
        Request request = new Request.Builder().url(httpUrl).get().build();
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(@NonNull Call call, @NonNull okhttp3.Response response) throws IOException {
                if(response.isSuccessful()){
                    String myResponse = response.body().string();
                    httpRequester.this.runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            textView.setText(myResponse);
                        }
                    });
                }
            }
        });
    }
}