package com.deeshank.notify.services;

import android.os.Bundle;
import android.util.Log;

import com.google.android.gms.gcm.GcmListenerService;

/**
 * Created by deeshank13 on 9/9/16.
 */
public class NotificationsListenerService extends GcmListenerService {

    private static final String TAG = "NotifyIntentService";

    @Override
    public void onMessageReceived(String from, Bundle data) {
        String message = data.getString("message");
        Log.d(TAG, message);
    }

}
