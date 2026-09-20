import discord


class ReportEmbedMessages:
    @staticmethod
    def report_embed_message_page_1(user: discord.Member) -> discord.Embed:
        """
        Creates an embed when /support report is invoked. This is page one of the report

        Args:
            user (discord.user): The discord user being reported

        Retruns:
            discord.Embed
        """
        embed_message = discord.Embed(
            title="Report",
            description="# Please pick one of the options below.",
        )
        embed_message.add_field(
            name="Proceed: ", value="Continue reporting your issue", inline=True
        )
        embed_message.add_field(
            name="Cancel: ", value="Stop with your report", inline=True
        )
        embed_message.add_field(name="Help: ", value="How to report", inline=True)
        embed_message.add_field(name="You are reporting", value=f"{user}", inline=True)
        embed_message.set_footer(
            text="All buttons will time out after 5 minutes. You are currently on step 1/x"
        )
        return embed_message

    @staticmethod
    def report_embed_message_page_2(user: discord.Member) -> discord.Embed:
        """
        Creates an embed when /support report is invoked. This is page two of the report

        Args:
            user (discord.user): The discord user being reported

        Retruns:
            discord.Embed
        """
        embed_message = discord.Embed(title="User")
        embed_message.add_field(name="You are reporting", value=f"{user}", inline=True)
        embed_message.set_footer(text="You are currently on step 2/x.")
        return embed_message
