﻿package com.sulake.habbo.communication.messages.incoming.inventory.achievements
{
    import com.sulake.core.communication.messages.MessageEvent;
    import com.sulake.core.communication.messages.IMessageEvent;
    import com.sulake.habbo.communication.messages.parser.inventory.achievements.AchievementsScoreMessageParser;

    public class AchievementsScoreEvent extends MessageEvent implements IMessageEvent 
    {

        public function AchievementsScoreEvent(param1:Function)
        {
            super(param1, AchievementsScoreMessageParser);
        }

        public function getParser():AchievementsScoreMessageParser
        {
            return (var_334 as AchievementsScoreMessageParser);
        }


    }
}