﻿package com.sulake.habbo.communication.messages.outgoing.notifications
{
    import com.sulake.core.communication.messages.IMessageComposer;
    import com.sulake.core.runtime.IDisposable;

    public class ResetUnseenItemsComposer implements IMessageComposer, IDisposable 
    {

        private var var_2493:Array = new Array();

        public function ResetUnseenItemsComposer(param1:int)
        {
            this.var_2493.push(param1);
        }

        public function getMessageArray():Array
        {
            return (this.var_2493);
        }

        public function dispose():void
        {
            this.var_2493 = null;
        }

        public function get disposed():Boolean
        {
            return (false);
        }


    }
}