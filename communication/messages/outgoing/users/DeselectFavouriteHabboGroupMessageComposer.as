﻿package com.sulake.habbo.communication.messages.outgoing.users
{
    import com.sulake.core.communication.messages.IMessageComposer;

    public class DeselectFavouriteHabboGroupMessageComposer implements IMessageComposer 
    {

        private var _data:Array = [];

        public function DeselectFavouriteHabboGroupMessageComposer(param1:int)
        {
            this._data.push(param1);
        }

        public function getMessageArray():Array
        {
            return (this._data);
        }

        public function dispose():void
        {
            this._data = null;
        }


    }
}